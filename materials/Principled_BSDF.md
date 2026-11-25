# Principled BSDF Node: Complete Guide (Blender)

> Based on the node shown in your screenshot (Blender 4.2+ layout, with the **Thin Film** panel and the **Diffuse > Roughness** field).

---

## Table of Contents

1. [What is the Principled BSDF?](#1-what-is-the-principled-bsdf)
2. [Key Concepts You Need First](#2-key-concepts-you-need-first)
3. [Node Output](#3-node-output)
4. [Main (Top-Level) Inputs](#4-main-top-level-inputs)
5. [Diffuse Panel](#5-diffuse-panel)
6. [Subsurface Panel](#6-subsurface-panel)
7. [Specular Panel](#7-specular-panel)
8. [Transmission Panel](#8-transmission-panel)
9. [Coat Panel](#9-coat-panel)
10. [Sheen Panel](#10-sheen-panel)
11. [Emission Panel](#11-emission-panel)
12. [Thin Film Panel](#12-thin-film-panel)
13. [How the Layers Combine](#13-how-the-layers-combine)
14. [Material Recipes (Presets)](#14-material-recipes-presets)
15. [Cycles vs EEVEE Notes](#15-cycles-vs-eevee-notes)
16. [Common Mistakes and Tips](#16-common-mistakes-and-tips)
17. [Quick Reference Table](#17-quick-reference-table)

---

## 1. What is the Principled BSDF?

**BSDF** = *Bidirectional Scattering Distribution Function*. It describes how light that hits a surface is reflected, refracted, or scattered.

The **Principled BSDF** is Blender's "all-in-one" **physically based rendering (PBR)** shader. It is based on the Disney/Pixar PBR model and combines many shader types into a single node:

- Diffuse (matte surfaces)
- Metallic reflection
- Glossy/specular reflection
- Glass-like transmission
- Subsurface scattering (skin, wax, marble)
- Clear coat (car paint)
- Sheen (cloth, velvet)
- Emission (glowing surfaces)
- Thin film iridescence (soap bubbles, oil slicks)

**Why use it?** With a single node you can create ~90% of real-world materials, and it plugs directly into the **Material Output** node.

---

## 2. Key Concepts You Need First

| Term | Meaning |
|---|---|
| **PBR** | Physically Based Rendering: materials behave like real-world materials under any lighting. |
| **Dielectric** | Non-metal (plastic, wood, skin, glass). Reflects a little light at glancing angles. |
| **Conductor** | Metal. Reflects almost all light and tints the reflection with its color. |
| **Fresnel** | Surfaces become more reflective at grazing angles (look at a lake from far away vs. straight down). |
| **IOR** | *Index of Refraction*: how much light bends and how reflective the surface is. |
| **Roughness** | Micro-surface bumpiness. 0 = mirror-sharp, 1 = fully blurry/matte. |
| **Socket colors** | Yellow = color, Grey = float (number), Purple = vector (normals), Green = shader. |

---

## 3. Node Output

### BSDF (green socket, top right)
The final shader result. Connect it to the **Surface** input of the **Material Output** node (or mix it with other shaders using Mix Shader / Add Shader).

---

## 4. Main (Top-Level) Inputs

### 4.1 Base Color
- **Type:** Color (yellow socket). **Screenshot value:** near-white.
- The main "paint" color of the surface.
  - For **non-metals**: the diffuse (matte) color.
  - For **metals**: the color of the reflection (e.g., gold = yellow-orange).
- **Tip:** Plug an **Image Texture** (albedo/diffuse map) here. Avoid pure black (0) or pure white (1); real materials sit between about 0.02 and 0.9.

### 4.2 Metallic
- **Range:** 0 to 1. **Screenshot value:** 0.000.
- Blends between a **dielectric** (0) and a **metal** (1).
- `0` = plastic, wood, skin, stone. `1` = steel, gold, copper.
- **Rule:** Real materials are almost always **0 or 1**. Use in-between values only for transitions (rust, dirt on metal, edge wear). Usually driven by a texture mask.

### 4.3 Roughness
- **Range:** 0 to 1. **Screenshot value:** 0.500.
- Controls how blurry the specular reflection is.
  - `0.0` = perfect mirror
  - `0.1 to 0.3` = polished/glossy
  - `0.5` = semi-gloss (default)
  - `1.0` = fully matte
- Often driven by a grayscale texture for realistic variation (scratches, fingerprints).

### 4.3b IOR (Index of Refraction)
- **Range:** 1 to 1000 (practical: 1 to 3). **Screenshot value:** 1.500.
- Controls how light bends going through the material and how strong the reflection is.
- Common values:

| Material | IOR |
|---|---|
| Air | 1.000 |
| Water | 1.333 |
| Ice | 1.31 |
| Plastic | 1.45 to 1.5 |
| Glass | 1.45 to 1.52 |
| Diamond | 2.417 |

- Mainly matters for **Transmission** (glass/liquids). For opaque surfaces use **Specular > IOR Level** instead.

### 4.4 Alpha
- **Range:** 0 to 1. **Screenshot value:** 1.000.
- Surface opacity. `1` = fully opaque, `0` = fully transparent.
- Different from Transmission: Alpha simply **hides** the surface (like a cut-out/leaf); Transmission **refracts** light through a volume (glass).
- In **EEVEE**, check the material's *Render Method / Blend Mode* settings for alpha to behave correctly.

### 4.5 Thin Wall (checkbox)
- **Screenshot:** unchecked.
- When enabled, the surface is treated as an infinitely thin sheet (no volume inside): light passes straight through **without refracting**.
- Use for: window panes, soap bubbles, paper, leaves, thin plastic film.
- Also much cheaper to render than a thick glass object.

### 4.6 Normal
- **Type:** Vector (purple socket).
- Overrides the surface normal direction to fake fine detail (bumps, dents) without extra geometry.
- Connect a **Normal Map** node (for normal-map textures) or a **Bump** node (for height/grayscale textures).
- If left empty, the mesh's own normals are used.

---

## 5. Diffuse Panel

### Roughness (Diffuse)
- **Screenshot value:** 0.000.
- Controls how rough the **diffuse (matte)** component is, separate from the specular roughness above.
- `0` = standard **Lambertian** diffuse (smooth, even matte).
- Higher values use an **Oren-Nayar**-style model: the surface looks flatter and "dustier" with a brighter edge falloff (like clay, moon surface, chalk, rough plaster).
- **Note:** This field only appears in newer Blender versions (about 4.3/4.4 and later).

---

## 6. Subsurface Panel

**Subsurface Scattering (SSS)** simulates light entering a surface, bouncing inside, and exiting at a different point. This gives a soft, "glowy" look.

**Used for:** skin, wax, milk, marble, jade, leaves, fruit flesh, candles.

### 6.1 Method dropdown (screenshot: *Random Walk*)
| Method | Description |
|---|---|
| **Random Walk** | Most accurate. Simulates actual light paths inside volume; handles thin geometry well. Default. |
| **Random Walk (Skin)** | A variant tuned for realistic skin; handles Radius with more physical behavior. |
| **Christensen-Burley** *(older versions)* | Faster approximation, less accurate. |

### 6.2 Weight
- **Screenshot value:** 0.000 (SSS is **off**).
- Blend amount between diffuse (0) and subsurface (1). Most materials use 0 or 1.

### 6.3 Radius (R, G, B)
- **Screenshot values:** 1.000 / 0.200 / 0.100.
- How far each color channel of light travels inside the material.
- Larger = more translucent for that color.
- **Default (1, 0.2, 0.1)** gives a reddish glow because red travels furthest: perfect for **skin** (blood/flesh scatters red).
- For milk/marble use roughly equal values; for green leaves push green higher.

### 6.4 Scale
- **Screenshot value:** 0.005 m.
- Multiplier for the Radius, in scene units.
- Increase for larger objects, decrease for small details. Must match your scene scale: a 2 m statue and a 2 cm ring need very different values.
- *(Blender's stock default is 0.05 m; yours is set smaller.)*

### 6.3b IOR (appears in some versions)
- Controls how light bends at the SSS boundary (Random Walk Skin method).

### 6.5 Anisotropy
- **Range:** 0 to 1. **Screenshot value:** 0.000.
- Direction bias of scattering inside the volume.
  - `0` = scatters equally in all directions.
  - Higher = light tends to continue **forward** through the material (more translucent look).

---

## 7. Specular Panel

Controls the **reflection** on non-metal surfaces. (Metals use Base Color for reflection tint.)

### 7.1 Distribution dropdown (screenshot: *Multiscatter GGX*)
| Option | Description |
|---|---|
| **GGX** | Standard microfacet distribution; fast. Can look slightly dark on very rough surfaces because light that bounces between microfacets is lost. |
| **Multiscatter GGX** | Adds multiple-bounce light between microfacets. More **energy-conserving** and brighter on rough surfaces; slightly slower. Best default. |

### 7.2 IOR Level
- **Range:** 0 to 1. **Screenshot value:** 0.500.
- A multiplier on the strength of specular reflection.
  - `0.5` = unchanged, physically correct (the default).
  - `0` = no specular reflection.
  - `1` = doubled reflection strength.
- Use a texture here as a **specular map** (e.g., dull dirty patches vs. shiny clean spots).

### 7.3 Tint
- **Type:** Color. **Screenshot:** white.
- Tints the reflection color at normal-facing angles for **non-metals**. White = no tint.
- Real dielectrics reflect *uncolored* light, so leave white unless doing something stylized.

### 7.4 Anisotropic
- **Range:** 0 to 1. **Screenshot value:** 0.000.
- Stretches the highlight in one direction instead of a round dot.
- **Examples:** brushed metal, hair, CDs, vinyl records, satin pans.
- `0` = isotropic (round highlight). Higher = more stretched.

### 7.5 Anisotropic Rotation
- **Range:** 0 to 1 (0 to 360 degrees). **Screenshot value:** 0.000.
- Rotates the stretch direction of the anisotropic highlight.

### 7.6 Tangent
- **Type:** Vector (purple socket).
- Custom tangent direction for anisotropy. If empty, it uses the **UV map** tangent.
- Use a **Tangent** node (Radial or UV Map) to create circular brushing (e.g., on a pot lid or CD).

---

## 8. Transmission Panel

### Weight
- **Range:** 0 to 1. **Screenshot value:** 0.000.
- Blends between opaque (0) and **fully transparent refracting** (1) material.
- Used for **glass, water, clear plastic, gems, ice**.
- Uses **IOR** (main section) for bending and **Roughness** for frosted look.
  - Glass: Transmission 1, Roughness 0, IOR 1.45
  - Frosted glass: Transmission 1, Roughness 0.3 to 0.5
- **Base Color** tints the transmitted light (colored glass).
- Compared to **Alpha**: Transmission **bends** light; Alpha merely hides.

---

## 9. Coat Panel

A **clear lacquer layer** on top of the base material (formerly called "Clearcoat").

**Used for:** car paint, varnished wood, lacquer, wet surfaces, glazed ceramic, carbon fiber.

### 9.1 Weight
- **Screenshot value:** 0.000 (off).
- Strength of the coat layer. `1` = full coat.

### 9.2 Roughness
- **Screenshot value:** 0.030.
- Roughness of the coat itself; very low by default, so it looks glossy.

### 9.3 IOR
- **Screenshot value:** 1.500.
- Refractive index of the coat (1.5 is typical for lacquers/varnish).

### 9.4 Tint
- **Type:** Color. **Screenshot:** white.
- Colors the coat layer and the light passing through it (tinted candy paint).

### 9.5 Normal
- **Type:** Vector.
- Separate normal for the coat. Lets the base layer be bumpy while the coat stays smooth (e.g., orange-peel paint, wet bumpy surfaces).

---

## 10. Sheen Panel

Adds a soft, **velvety light-scattering layer** at glancing angles, simulating tiny fibers.

**Used for:** cloth, velvet, satin, peach fuzz, dust.

### 10.1 Weight
- **Screenshot value:** 0.000.
- Intensity of the sheen layer.

### 10.2 Roughness
- **Screenshot value:** 0.500.
- Spread of the sheen. Low = narrow and tight at edges; high = broader and softer.

### 10.3 Tint
- **Type:** Color. **Screenshot:** white.
- Color of the sheen glow (often a lighter version of the fabric color).

---

## 11. Emission Panel

Makes the surface **emit light** (glow).

### 11.1 Color
- **Screenshot:** white.
- The color of the emitted light.

### 11.2 Strength
- **Screenshot value:** 0.000 (no glow).
- Brightness (in W/m² for Cycles).
- `1` = soft glow. `10 to 100+` = bright light source (screens, neon, lava, lamps).
- In **Cycles**, emissive meshes actually **illuminate** nearby objects. In **EEVEE** they glow but need Bloom or light probes for light spill (version dependent).

---

## 12. Thin Film Panel

*(New in Blender 4.2.)* Simulates **thin-film interference**, where light waves bouncing off the top and bottom of a very thin transparent layer interfere and create rainbow colors.

**Used for:** soap bubbles, oil on water, beetle shells, anodized metals, pearls, CDs, heat-tempered steel.

### 12.1 Thickness
- **Screenshot value:** 0 nm (off).
- Film thickness in **nanometers**. Visible effects occur around **100 to 1000 nm**.
- Different thickness = different rainbow colors. **Drive with a noise texture** for realistic swirling bubbles/oil.

### 12.2 IOR
- **Screenshot value:** 1.330.
- IOR of the thin film layer (1.33 = water-like, good for soap bubbles).

---

## 13. How the Layers Combine

Conceptually, light interacts with the layers **in this stacking order (top to bottom)**:

```
        Incoming light
              │
   ┌──────────▼──────────┐
   │  Thin Film          │  rainbow interference
   ├─────────────────────┤
   │  Coat               │  clear lacquer
   ├─────────────────────┤
   │  Sheen              │  fabric fuzz
   ├─────────────────────┤
   │  Specular           │  glossy reflection (dielectric)
   ├─────────────────────┤
   │  Transmission       │  see-through refraction
   │  Subsurface         │  light scattering inside
   │  Diffuse            │  matte base color
   │  Metallic           │  replaces diffuse with metal reflection
   └─────────────────────┘
   + Emission added on top (glow)
```

Key interactions:
- **Metallic = 1** removes diffuse, subsurface, and transmission: the surface becomes pure metal reflection tinted by Base Color.
- **Transmission** takes priority over diffuse/subsurface for the non-metal part.
- **Alpha** blends the entire result with transparency at the very end.
- **Emission** is simply added to the final result.

---

## 14. Material Recipes (Presets)

| Material | Base Color | Metallic | Roughness | Other Settings |
|---|---|---|---|---|
| **Clear glass** | White | 0 | 0 | Transmission Weight 1, IOR 1.45 |
| **Frosted glass** | White | 0 | 0.4 | Transmission 1, IOR 1.45 |
| **Polished gold** | (1.0, 0.77, 0.34) | 1 | 0.1 to 0.2 | none |
| **Brushed steel** | Grey (0.6) | 1 | 0.35 | Specular Anisotropic 0.8 |
| **Plastic (glossy)** | Any | 0 | 0.15 | Coat optional |
| **Rubber** | Dark grey | 0 | 0.8 | IOR Level 0.3 |
| **Skin** | Skin tone | 0 | 0.4 | Subsurface Weight 1, Radius (1, 0.2, 0.1), Scale 0.01 to 0.05 |
| **Car paint** | Any color | 0 or 0.5 | 0.4 | Coat Weight 1, Coat Roughness 0.03 |
| **Velvet / cloth** | Any color | 0 | 0.8 | Sheen Weight 1, Sheen Roughness 0.3 |
| **Neon light** | Black | 0 | 0.5 | Emission color + Strength 10 to 50 |
| **Wax / candle** | Cream | 0 | 0.3 | Subsurface Weight 1, larger Radius |
| **Soap bubble** | White | 0 | 0 | Thin Wall on, Transmission 1, Thin Film thickness 300 to 600 nm |
| **Water** | White | 0 | 0 | Transmission 1, IOR 1.333 |
| **Diamond** | White | 0 | 0 | Transmission 1, IOR 2.417 |

---

## 15. Cycles vs EEVEE Notes

| Feature | Cycles | EEVEE |
|---|---|---|
| Subsurface | Full Random Walk volume simulation | Approximated screen-space blur |
| Transmission | Accurate refraction | Approximated (needs screen-space refraction / raytracing setting) |
| Thin Film | Supported | Support depends on version |
| Emission lighting | Lights other objects | Glows; light spill needs raytracing/probes |
| Anisotropy / Multiscatter | Supported | Supported (approximations) |
| Speed | Slower, more accurate | Real-time |

---

## 16. Common Mistakes and Tips

1. **Using in-between Metallic values** for normal materials. Stick with 0 or 1.
2. **Color maps in the wrong color space.** Color textures (Base Color) use *sRGB*; data maps (Roughness, Metallic, Normal, Bump) must be **Non-Color**.
3. **Pure black or white Base Color.** Real materials are rarely 0 or 1; avoid extremes.
4. **Subsurface scale mismatch.** If SSS looks too weak or too strong, adjust **Scale** to suit object size.
5. **Using Alpha for glass.** Use **Transmission** instead, and Alpha only for cutouts.
6. **Forgetting Thin Wall** for flat glass panes (renders faster and avoids weird refraction).
7. **Not driving values with textures.** Variation in Roughness is the biggest realism boost.
8. **Roughness 0 with Transmission** can render noisy in Cycles; try 0.01 to 0.02.
9. **Normal map strength.** Use the Normal Map node's *Strength* to dial detail up or down.

---

## 17. Quick Reference Table

| Panel | Input | Type | Your Value | Purpose |
|---|---|---|---|---|
| Main | Base Color | Color | White | Surface color |
| Main | Metallic | Float | 0.0 | Non-metal / metal |
| Main | Roughness | Float | 0.5 | Reflection blur |
| Main | IOR | Float | 1.5 | Light bending |
| Main | Alpha | Float | 1.0 | Opacity |
| Main | Thin Wall | Bool | Off | Thin sheet mode |
| Main | Normal | Vector | none | Surface detail |
| Diffuse | Roughness | Float | 0.0 | Matte roughness |
| Subsurface | Method | Enum | Random Walk | SSS algorithm |
| Subsurface | Weight | Float | 0.0 | SSS amount |
| Subsurface | Radius | Vector | 1, 0.2, 0.1 | Scatter distance per color |
| Subsurface | Scale | Float | 0.005 m | Radius multiplier |
| Subsurface | Anisotropy | Float | 0.0 | Scatter direction bias |
| Specular | Distribution | Enum | Multiscatter GGX | Reflection model |
| Specular | IOR Level | Float | 0.5 | Reflection strength |
| Specular | Tint | Color | White | Reflection tint |
| Specular | Anisotropic | Float | 0.0 | Stretched highlights |
| Specular | Anisotropic Rotation | Float | 0.0 | Highlight direction |
| Specular | Tangent | Vector | none | Custom stretch direction |
| Transmission | Weight | Float | 0.0 | Glass amount |
| Coat | Weight | Float | 0.0 | Lacquer layer |
| Coat | Roughness | Float | 0.03 | Coat blur |
| Coat | IOR | Float | 1.5 | Coat refraction |
| Coat | Tint | Color | White | Coat color |
| Coat | Normal | Vector | none | Coat surface detail |
| Sheen | Weight | Float | 0.0 | Fabric fuzz |
| Sheen | Roughness | Float | 0.5 | Fuzz spread |
| Sheen | Tint | Color | White | Fuzz color |
| Emission | Color | Color | White | Glow color |
| Emission | Strength | Float | 0.0 | Glow brightness |
| Thin Film | Thickness | Float | 0 nm | Rainbow film thickness |
| Thin Film | IOR | Float | 1.33 | Film refraction |

---

### Summary of Your Current Setup

Your node is essentially the **default Principled BSDF**: a plain, slightly glossy, non-metallic, opaque white material (Metallic 0, Roughness 0.5, IOR 1.5) with **every optional layer switched off** (Subsurface, Transmission, Coat, Sheen, Emission, and Thin Film all at weight/strength 0). Turn up only the layers you need to build your material.
