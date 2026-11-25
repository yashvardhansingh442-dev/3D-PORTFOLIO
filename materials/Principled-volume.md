# Principled Volume Node: Complete Guide (Blender)

> Based on your screenshot of the default Principled Volume node.

---

## Table of Contents

1. [What is the Principled Volume?](#1-what-is-the-principled-volume)
2. [Key Concepts You Need First](#2-key-concepts-you-need-first)
3. [How to Set It Up (Important)](#3-how-to-set-it-up-important)
4. [Node Output](#4-node-output)
5. [Scattering Inputs](#5-scattering-inputs)
6. [Absorption Input](#6-absorption-input)
7. [Emission Inputs](#7-emission-inputs)
8. [Blackbody (Fire) Inputs](#8-blackbody-fire-inputs)
9. [Attribute Fields Explained](#9-attribute-fields-explained)
10. [How Light Behaves Inside the Volume](#10-how-light-behaves-inside-the-volume)
11. [Volume Recipes (Presets)](#11-volume-recipes-presets)
12. [Principled Volume vs Other Volume Nodes](#12-principled-volume-vs-other-volume-nodes)
13. [Cycles vs EEVEE Notes](#13-cycles-vs-eevee-notes)
14. [Common Mistakes and Tips](#14-common-mistakes-and-tips)
15. [Quick Reference Table](#15-quick-reference-table)

---

## 1. What is the Principled Volume?

The **Principled Volume** is Blender's all-in-one shader for **volumetric materials**: things that have *depth and fill space* instead of just a surface.

It combines three behaviors in one node:

- **Scattering**: light bounces around inside (fog, smoke, clouds, milk)
- **Absorption**: light is soaked up as it travels (dark smoke, tinted liquids)
- **Emission**: the volume itself glows (fire, explosions, nebulae, glowing gas)

**Use it for:** smoke, fire, fog, mist, clouds, steam, dust, atmosphere, nebulae, explosions, light shafts (god rays), and imported volumetric data such as OpenVDB files.

---

## 2. Key Concepts You Need First

| Term | Meaning |
|---|---|
| **Volume** | A material that exists *inside* an object's space, not just on its skin. |
| **Density** | How "thick" the medium is. More density = more light is scattered or absorbed per unit distance. |
| **Scattering** | Light changes direction when it hits particles in the medium (why fog looks white and visible). |
| **Absorption** | Light energy is removed (why dark smoke is dark). |
| **Anisotropy** | Whether scattered light prefers going forward, backward, or equally in all directions. |
| **Attribute** | Per-voxel data stored in a volume (density, color, temperature, etc.), often from a smoke/fire simulation or a VDB file. |
| **Blackbody** | The glow of a hot object, based on its temperature (fire, hot metal, lava). |
| **Kelvin (K)** | Temperature unit. About 1000 K is deep red, 1500 K orange, 3000 K warm yellow, 6500 K white, 10000 K+ bluish. |

---

## 3. How to Set It Up (Important)

This is the most common beginner confusion.

1. The Principled Volume output plugs into the **Volume** socket of the **Material Output** node, **not** the Surface socket.
2. The object should usually be a **closed mesh** (like a cube) used as a *container/domain* for the volume.
3. Leave the **Surface** socket empty (or the object's surface may block or tint the view). An empty surface makes the container invisible, so you see only the volume inside.
4. For simulation domains (smoke/fire), Blender sets up a Principled Volume automatically.

```
 [Principled Volume] ──Volume──▶ [Material Output: Volume socket]
                                 [Material Output: Surface socket = empty]
```

---

## 4. Node Output

### Volume (green socket, top right)
The finished volumetric shader. Connect it to the **Volume** input of **Material Output** (or to a **Mix Shader / Add Shader** to combine with other volume nodes).

---

## 5. Scattering Inputs

### 5.1 Color
- **Type:** Color (yellow socket). **Screenshot:** light grey.
- The **scattering color**: the color of the medium when lit.
- White/grey = classic fog, smoke, cloud. Colored = tinted smoke, colored mist.
- **Tip:** For realistic clouds and mist use near-white.

### 5.2 Color Attribute
- **Type:** Text field (name of an attribute). **Screenshot:** empty.
- If you enter an attribute name (for example `color`), the color of the volume is **read per-voxel from that attribute**.
- Leave empty to use the single **Color** value everywhere.
- Useful for volumes where each point has its own color (simulation data or VDB files).

### 5.3 Density
- **Range:** 0 and up. **Screenshot value:** 1.000.
- The overall **thickness** of the volume.
  - `0` = nothing (invisible)
  - `0.01 to 0.1` = thin fog or mist
  - `1` = fairly dense smoke or cloud
  - `10+` = very thick, nearly solid-looking
- This value **multiplies** the density attribute (see Section 9).
- **Tip:** Density is very sensitive. A big visual change can come from small adjustments, so tune it in small steps (especially for large fog volumes).

### 5.4 Density Attribute
- **Type:** Text field. **Screenshot:** `density`.
- The name of the per-voxel attribute that stores density. `density` is the standard name used by smoke simulations and many VDB files.
- If the object has no such attribute, the node uses a **uniform density** equal to the Density value.
- You can change it to read a different attribute (for example `heat`, `flame`, or a custom name).

### 5.5 Anisotropy
- **Range:** -1 to 1. **Screenshot value:** 0.000.
- Controls the **direction scattered light prefers** (the phase function).
  - `0` = scatters equally in all directions (isotropic)
  - **Positive** (up to 1) = **forward scattering**: light keeps going the way it was traveling. Looks bright when you look toward the light, like backlit mist or sun glow through clouds.
  - **Negative** (down to -1) = **backward scattering**: light bounces back toward the source.
- **Typical values:** 0.3 to 0.8 for fog/cloud/smoke look (they are strongly forward scattering in real life).

---

## 6. Absorption Input

### Absorption Color
- **Type:** Color (yellow socket). **Screenshot:** black.
- Adds **absorption** on top of scattering: light passing through is darkened and tinted by this color.
- **Black (default)** = no extra absorption; the volume only scatters.
- Brighter/more saturated values absorb more of that color. Real-world examples:
  - Dark soot smoke: a bright/grey absorption color
  - Tinted liquids or colored gas: a saturated color
- Often combined with scattering to create **dark smoke** (grey Absorption Color + low-ish scatter Color).

---

## 7. Emission Inputs

These make the volume **glow by itself**.

### 7.1 Emission Strength
- **Range:** 0 and up. **Screenshot value:** 0.000 (no glow).
- The brightness of the volume's own light.
  - `0` = does not glow
  - `1 to 5` = soft glow
  - `10+` = very bright (explosion, plasma)
- In **Cycles**, an emissive volume also **lights nearby objects**.

### 7.2 Emission Color
- **Type:** Color (yellow socket). **Screenshot:** white.
- The color of the glow. Use orange/red for fire, blue/purple for magic, and green for toxic gas.
- This is a **flat color glow**. For realistic fire color from temperature, use Blackbody (next section).

---

## 8. Blackbody (Fire) Inputs

A **blackbody** glows according to its temperature, just like real fire, hot metal, or lava. This gives physically believable fire colors automatically.

### 8.1 Blackbody Intensity
- **Range:** 0 to 1 (can go higher). **Screenshot value:** 0.000 (off).
- How strongly the **temperature-based glow** is applied.
- `0` = no blackbody glow. Higher = stronger fire-like emission.
- It works together with Emission Strength (the glow also scales with brightness controls). If you see no fire, check both values.

### 8.2 Blackbody Tint
- **Type:** Color (yellow socket). **Screenshot:** white.
- Multiplies the blackbody glow color.
- White = pure physical blackbody color. Use another color to stylize (for example green flame).

### 8.3 Temperature
- **Screenshot value:** 1000 K.
- The temperature of the blackbody in **Kelvin**, which determines glow color:

| Temperature | Glow color |
|---|---|
| About 800 to 1000 K | Dim red |
| About 1500 K | Orange (candle/campfire) |
| About 2500 to 3000 K | Yellow-orange (hot flame) |
| About 5000 to 6500 K | White |
| 8000 K and higher | Bluish-white |

- When a **Temperature Attribute** exists in the volume (like a fire simulation), the volume's temperature data is used and this value acts together with it. Check the Blender manual for the exact behavior in your version, and tune by eye.

### 8.4 Temperature Attribute
- **Type:** Text field. **Screenshot:** `temperature`.
- The name of the per-voxel attribute that stores temperature. `temperature` is the standard name in Blender's fire simulations (Quick Smoke/Quick Explode with fire enabled).
- If no such attribute exists, the single Temperature value is used everywhere.

---

## 9. Attribute Fields Explained

The text-field inputs (**Color Attribute**, **Density Attribute**, **Temperature Attribute**) connect the node to **data stored inside the volume**.

| Field | Default name | Typical source | Result |
|---|---|---|---|
| Color Attribute | *(empty)* | VDB or simulation with color data | Per-voxel color |
| Density Attribute | `density` | Smoke simulation, VDB | Shape and thickness of the smoke |
| Temperature Attribute | `temperature` | Fire simulation, VDB | Where the fire glows hot |

**Behavior to remember:**
- If an attribute **exists**, it drives that property per voxel.
- If it **does not exist**, the node falls back to the single value (uniform fog).
- That is why a plain cube with this material gives **uniform fog**, but a smoke simulation domain gives **detailed smoke**.

---

## 10. How Light Behaves Inside the Volume

Light traveling through the volume can:

```
   Incoming light
        │
        ▼
 ┌────────────────────────┐
 │  Absorbed              │ ← Absorption Color (darkens/tints)
 │  Scattered             │ ← Color, Density, Anisotropy (direction)
 │  Passes straight       │
 │  + Volume's own glow   │ ← Emission / Blackbody (adds light)
 └────────────────────────┘
        │
        ▼
   What the camera sees
```

- **Density** controls how often these interactions happen.
- **Color** and **Absorption Color** decide what is scattered vs absorbed.
- **Anisotropy** decides the scatter direction.
- **Emission and Blackbody** add light on top.

---

## 11. Volume Recipes (Presets)

| Effect | Color | Density | Anisotropy | Absorption | Emission | Notes |
|---|---|---|---|---|---|---|
| **Light fog / mist** | White | 0.02 to 0.1 | 0.3 | Black | 0 | Big cube around the scene |
| **Dense fog** | White | 0.3 to 1 | 0.4 | Black | 0 | |
| **Cloud** | White | 5 to 20 | 0.5 to 0.8 | Black | 0 | Use VDB or textured density |
| **White smoke** | Light grey | 1 to 5 | 0.2 | Black | 0 | Smoke simulation |
| **Dark soot smoke** | Grey | 2 to 10 | 0.1 | Grey/bright | 0 | Absorption darkens it |
| **Fire** | Black or very dark | 1 to 5 | 0 | Black | Strength 2 to 10 | Blackbody Intensity 1, Temperature 1500 to 3000 K |
| **Explosion** | Dark grey | 3 to 10 | 0.2 | Some | Higher | Blackbody + smoke |
| **Magic / energy glow** | Any | 0.5 to 2 | 0 | Black | Strength 3 to 10 | Colored Emission Color |
| **God rays (light shafts)** | White | 0.01 to 0.05 | 0.5 to 0.8 | Black | 0 | Needs a strong light (spot or sun) shining into the volume |
| **Tinted liquid / colored gas** | Any color | 1 to 5 | 0 | Same hue | 0 | |
| **Nebula** | Any | Textured | 0 | Black | Low | Use a noise texture to drive density |

*(These are starting points to tweak by eye.)*

---

## 12. Principled Volume vs Other Volume Nodes

| Node | What it does |
|---|---|
| **Principled Volume** | All-in-one: scatter, absorb, emit, blackbody, attributes |
| **Volume Scatter** | Scattering only (Color, Density, Anisotropy) |
| **Volume Absorption** | Absorption only (Color, Density) |
| **Emission** (volume use) | Glow only |
| **Volume Coefficients** | Direct control of scatter/absorption coefficients (advanced) |

Use the **Principled Volume** for most work. Use the simpler nodes when you want precise control over one effect or a lighter, simpler setup.

---

## 13. Cycles vs EEVEE Notes

| Feature | Cycles | EEVEE |
|---|---|---|
| Accuracy | Physically accurate light transport | Approximated |
| Volume lighting other objects | Yes (emission illuminates the scene) | Limited, depends on version and settings |
| Render time | Slower; dense volumes can be expensive | Fast, real-time preview |
| Setup | Works directly | Volume quality settings (resolution, samples) matter |

In **EEVEE**, if volumes look blocky or banded, raise the volume resolution and sample settings in Render Properties.

---

## 14. Common Mistakes and Tips

1. **Plugged into Surface instead of Volume.** The volume shows nothing or acts like a solid surface. Use the **Volume** socket.
2. **Object looks like a solid box.** Make sure the Surface socket is empty and the object is a closed container.
3. **Density too high or too low.** Fog usually needs very small values (0.01 to 0.1); adjust in small steps.
4. **Fire does not glow.** Set **Blackbody Intensity** above 0 and/or **Emission Strength** above 0, and make sure a **temperature** attribute or a high enough **Temperature** exists.
5. **Smoke looks flat.** Raise Anisotropy slightly and add a strong backlight.
6. **Render takes forever.** Dense, large volumes are costly in Cycles. Reduce Density, volume bounces, or use a smaller domain. Use denoising.
7. **Attribute names misspelled.** Names are case-sensitive. If the name does not match, the node silently uses the uniform value.
8. **No light = no volume.** Volumes need lights or an environment to be visible (except emissive ones).
9. **Fog volume clipped at the edges.** Make the container larger than the area you are filming.

---

## 15. Quick Reference Table

| Group | Input | Type | Your Value | Purpose |
|---|---|---|---|---|
| Scattering | Color | Color | Light grey | Scattering color |
| Scattering | Color Attribute | Text | empty | Per-voxel color data name |
| Scattering | Density | Float | 1.000 | Thickness of medium |
| Scattering | Density Attribute | Text | `density` | Per-voxel density data name |
| Scattering | Anisotropy | Float | 0.000 | Scatter direction (-1 back, +1 forward) |
| Absorption | Absorption Color | Color | Black | Extra light absorption/tint |
| Emission | Emission Strength | Float | 0.000 | Glow brightness |
| Emission | Emission Color | Color | White | Glow color |
| Blackbody | Blackbody Intensity | Float | 0.000 | Strength of temperature glow |
| Blackbody | Blackbody Tint | Color | White | Tint of temperature glow |
| Blackbody | Temperature | Float (K) | 1000 K | Blackbody temperature |
| Blackbody | Temperature Attribute | Text | `temperature` | Per-voxel temperature data name |
| Output | Volume | Shader | n/a | Goes to Material Output (Volume) |

---

### Summary of Your Current Setup

Your node is the **default Principled Volume**: a light-grey, medium-density (1.0), non-directional scattering medium with **no extra absorption, no emission, and no blackbody glow**. It is basically a plain grey fog. To get **fog**, lower Density and raise Anisotropy. For **smoke**, add Absorption and a smoke simulation. For **fire**, raise Emission Strength and Blackbody Intensity and set a Temperature of about 1500 to 3000 K.
