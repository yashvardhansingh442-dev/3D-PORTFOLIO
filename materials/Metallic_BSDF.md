# Metallic BSDF Node: Complete Guide (Blender)

> Based on your three screenshots: the default node, the **Fresnel Type** dropdown, and the **Distribution** dropdown. This node is available in newer Blender versions (4.2+ layout, with the Thin Film panel).

---

## Table of Contents

1. [What is the Metallic BSDF?](#1-what-is-the-metallic-bsdf)
2. [Key Concepts You Need First](#2-key-concepts-you-need-first)
3. [Node Output](#3-node-output)
4. [Distribution Dropdown](#4-distribution-dropdown)
5. [Fresnel Type Dropdown](#5-fresnel-type-dropdown)
6. [Inputs in F82 Tint Mode](#6-inputs-in-f82-tint-mode)
7. [Inputs in Physical Conductor Mode](#7-inputs-in-physical-conductor-mode)
8. [Shared Inputs (Both Modes)](#8-shared-inputs-both-modes)
9. [Thin Film Panel](#9-thin-film-panel)
10. [F82 Tint vs Physical Conductor](#10-f82-tint-vs-physical-conductor)
11. [Metallic BSDF vs Principled BSDF](#11-metallic-bsdf-vs-principled-bsdf)
12. [Material Recipes](#12-material-recipes)
13. [Cycles vs EEVEE Notes](#13-cycles-vs-eevee-notes)
14. [Common Mistakes and Tips](#14-common-mistakes-and-tips)
15. [Quick Reference Table](#15-quick-reference-table)

---

## 1. What is the Metallic BSDF?

The **Metallic BSDF** is a dedicated shader for **pure metals**. It does one job: simulate how light reflects off a metal surface.

Unlike the **Principled BSDF**, it has **no** diffuse, subsurface, transmission, coat, sheen, or emission layers. It is a specialized, cleaner, faster node when you only need metal.

**Use it for:** steel, aluminium, gold, copper, silver, chrome, brass, brushed metal, anodized or heat-tinted metal (via Thin Film).

---

## 2. Key Concepts You Need First

| Term | Meaning |
|---|---|
| **Conductor** | A metal. Reflects most light and tints the reflection with its own color. |
| **Dielectric** | A non-metal (plastic, wood). Not what this node is for. |
| **Fresnel** | Reflectivity changes with viewing angle. At glancing angles all surfaces reflect more. |
| **F0** | Reflectivity when looking straight at the surface (0 degrees). This is the "color" of a metal. |
| **F82** | Reflectivity at about 82 degrees, near a grazing angle. Used to control edge color. |
| **IOR (n)** | Index of refraction. For metals it is a color (R, G, B), not a single number. |
| **Extinction (k)** | How strongly a metal absorbs light. Also a color (R, G, B). |
| **Roughness** | Micro-surface bumpiness. 0 = mirror, 1 = fully blurry. |
| **Anisotropy** | Stretching of the highlight in one direction (brushed metal). |

---

## 3. Node Output

### BSDF (green socket, top right)
The final shader. Connect it to the **Surface** socket of the **Material Output** node, or combine it with other shaders using **Mix Shader** / **Add Shader**.

---

## 4. Distribution Dropdown

*(Screenshot 3. Yours is set to **Multiscatter GGX**.)*

This chooses the **mathematical model** for how the microscopic bumps of the surface scatter light.

| Option | Description | When to use |
|---|---|---|
| **Beckmann** | An older microfacet model. Sharper highlight falloff, tighter "core" with a shorter tail. | Rarely needed. Cycles only; EEVEE usually approximates it with GGX. |
| **GGX** | The modern standard. Has a longer, softer tail on highlights, which looks realistic. Fast. | Good general choice and when speed matters. |
| **Multiscatter GGX** | GGX plus **multiple bounces** between microfacets. More **energy-conserving**: rough metals stay brighter and keep their color instead of going dark. Slightly slower. | **Best default**, especially for rough metals. |

**Why Multiscatter matters for metal:** Metals reflect so much light that the light lost in single-scatter models is very noticeable at high roughness. Multiscatter recovers this and gives a more saturated, correct result.

---

## 5. Fresnel Type Dropdown

*(Screenshot 2. Yours is set to **F82 Tint**.)*

This chooses **how the color and reflectivity of the metal are defined**. It changes which inputs the node shows.

| Option | How you describe the metal | Style |
|---|---|---|
| **F82 Tint** | By two **colors**: Base Color and Edge Tint | Artist-friendly, easy, great for textures |
| **Physical Conductor** | By **real measured optical constants** (IOR n and Extinction k) | Scientific, physically accurate |

---

## 6. Inputs in F82 Tint Mode

### 6.1 Base Color
- **Type:** Color (yellow socket). **Screenshot:** light warm grey.
- The color of the metal **when viewed head-on** (this is F0).
- Examples: gold is yellow-orange, copper is orange-red, steel is neutral grey, aluminium is light silver.
- **Tip:** Metals are bright. Keep values high (roughly 0.5 to 1.0), never dark. A dark Base Color gives a dull, dead-looking metal.
- Plug an albedo/color map here for painted or worn metal.

### 6.2 Edge Tint
- **Type:** Color (yellow socket). **Screenshot:** very light blue-white.
- The color of the reflection at **glancing (grazing) angles**, near the silhouette of the object (this is F82).
- Real metals do not simply turn white at the edges; their color shifts slightly. Edge Tint lets you control this.
- **Default (near white)** works for most metals. Change it for stylized or highly saturated metals such as gold or copper to get richer, more accurate edge color.
- If Edge Tint equals white, you get the classic Schlick Fresnel behavior (edges brighten toward white).

---

## 7. Inputs in Physical Conductor Mode

*(Select **Physical Conductor** in the Fresnel Type dropdown. Base Color and Edge Tint are replaced by these two.)*

### 7.1 IOR (n)
- **Type:** Color/Vector (R, G, B).
- The real part of the metal's complex refractive index, per color channel.

### 7.2 Extinction (k)
- **Type:** Color/Vector (R, G, B).
- The imaginary part: how strongly the metal absorbs light per channel. Metals have large values.

### Approximate reference values (RGB)

| Metal | IOR (n) R, G, B | Extinction (k) R, G, B |
|---|---|---|
| Gold | 0.18, 0.42, 1.37 | 3.42, 2.35, 1.77 |
| Copper | 0.27, 0.68, 1.22 | 3.61, 2.63, 2.29 |
| Silver | 0.16, 0.12, 0.14 | 4.83, 3.12, 2.15 |
| Aluminium | 1.35, 0.97, 0.62 | 7.47, 6.40, 5.30 |

> These are rounded, commonly quoted approximations. Look up measured data (for example on refractiveindex.info) for exact values.

**When to use:** Product visualization, scientific rendering, or whenever you want physically exact color and Fresnel behavior without hand-tuning colors.

---

## 8. Shared Inputs (Both Modes)

### 8.1 Roughness
- **Range:** 0 to 1. **Screenshot value:** 0.500.
- Controls how blurry the reflections are.
  - `0.0` = perfect mirror (chrome)
  - `0.1 to 0.3` = polished metal
  - `0.4 to 0.6` = satin/semi-gloss
  - `0.7 to 1.0` = rough, cast or sandblasted metal
- **Tip:** Drive it with a grayscale texture (scratches, fingerprints, wear) for the biggest realism boost.

### 8.2 Anisotropy
- **Range:** 0 to 1. **Screenshot value:** 0.000.
- Stretches the highlight along one direction instead of a round spot.
- `0` = round highlight (isotropic).
- Higher values = longer streaks, like **brushed metal**, pots and pans, CDs, hair-like finishes.

### 8.3 Rotation
- **Range:** 0 to 1 (maps to 0 to 360 degrees). **Screenshot value:** 0.000.
- Rotates the direction of the anisotropic stretch.
- Only has an effect when **Anisotropy is above 0**.

### 8.4 Normal
- **Type:** Vector (purple socket).
- Overrides the surface normal to add fine detail (dents, hammered texture, engraving) without extra geometry.
- Connect a **Normal Map** node (normal textures) or a **Bump** node (height maps).
- If empty, the mesh's own normals are used.

### 8.5 Tangent
- **Type:** Vector (purple socket).
- Defines the direction used for anisotropy.
- If empty, the **UV map** direction is used.
- Use a **Tangent** node (Radial mode) to create circular brushing, such as on a pot lid, coin, speaker cone, or CD.

---

## 9. Thin Film Panel

*(Collapsible panel at the bottom. New in Blender 4.2.)*

Simulates **thin-film interference**: a very thin transparent layer on top of the metal splits light, and the reflected waves interfere to create **rainbow colors**.

**Used for:** anodized titanium or aluminium, heat-tempered steel (blue/purple tint), oil film on metal, oxidized coatings, rainbow-finish chrome, beetle-shell-like metal.

### 9.1 Thickness
- **Screenshot value:** 0 nm (effect is **off**).
- Film thickness in **nanometers**.
- Visible effects appear at roughly **100 to 1000 nm**, and different thicknesses give different colors.
- **Tip:** Drive it with a noise texture for swirling, varied color.

### 9.2 IOR
- **Screenshot value:** 1.330.
- Refractive index of the thin film layer.
- 1.33 is water-like. Oxide layers are usually higher (around 1.5 to 2.5).

---

## 10. F82 Tint vs Physical Conductor

| Feature | F82 Tint | Physical Conductor |
|---|---|---|
| Inputs | Base Color, Edge Tint | IOR (n), Extinction (k) |
| Ease of use | Easy, artistic | Needs real data |
| Works with textures | Yes, plug in color maps directly | Awkward |
| Accuracy | Good approximation | Physically exact |
| Best for | Games, art, most projects, painted or worn metal | Scientific/product rendering, exact real metals |

---

## 11. Metallic BSDF vs Principled BSDF

| | Metallic BSDF | Principled BSDF (Metallic = 1) |
|---|---|---|
| Purpose | Pure metal only | Everything (all-in-one) |
| Layers | Reflection + Thin Film | Diffuse, SSS, Transmission, Coat, Sheen, Emission, etc. |
| Metal color control | Base Color + Edge Tint, or physical n/k | Base Color (+ Specular Tint) |
| Speed and simplicity | Lighter, cleaner | Heavier |
| Mixing metal and non-metal | Needs a Mix Shader | Built in (Metallic slider 0 to 1) |

**Rule of thumb:**
- Whole object is metal: **Metallic BSDF**.
- Material mixes metal and other things (rust, paint, dirt): **Principled BSDF** with a Metallic mask, or use **Mix Shader** with a Metallic BSDF and another shader.

---

## 12. Material Recipes

| Metal | Mode | Base Color | Edge Tint | Roughness | Notes |
|---|---|---|---|---|---|
| **Chrome** | F82 Tint | Light grey (0.9) | White | 0.02 | Needs a good HDRI to reflect |
| **Polished steel** | F82 Tint | Grey (0.6) | White | 0.15 | |
| **Brushed steel** | F82 Tint | Grey (0.6) | White | 0.35 | Anisotropy 0.8 |
| **Aluminium** | F82 Tint | Silver (0.9) | White | 0.25 | |
| **Gold** | F82 Tint | (1.0, 0.77, 0.34) | Light yellow | 0.15 | Or Physical Conductor with gold n/k |
| **Copper** | F82 Tint | (0.95, 0.64, 0.54) | Light orange | 0.2 | |
| **Rough cast iron** | F82 Tint | Dark grey (0.3) | White | 0.8 | |
| **Anodized titanium** | F82 Tint | Grey | White | 0.3 | Thin Film Thickness 200 to 500 nm |
| **Heat-tempered steel** | F82 Tint | Grey | White | 0.2 | Thin Film Thickness about 300 nm, IOR about 2 |
| **Rusty metal** | n/a | n/a | n/a | n/a | Mix Shader: Metallic BSDF + a rough dielectric, with a rust texture as the factor |

---

## 13. Cycles vs EEVEE Notes

| Feature | Cycles | EEVEE |
|---|---|---|
| Beckmann | Supported | Approximated (usually behaves like GGX) |
| GGX / Multiscatter GGX | Fully supported | Supported (approximations) |
| Anisotropy | Supported | Supported |
| Physical Conductor | Supported | Supported (version dependent) |
| Thin Film | Supported | Version dependent |
| Reflections | Accurate ray-traced | Depend on raytracing/probes setup |

**Important for metals:** A metal reflects its **surroundings**. With no environment (empty black world), a metal looks black. Always use an **HDRI** or add objects/lights for it to reflect.

---

## 14. Common Mistakes and Tips

1. **Metal looks black or dull.** Almost always a lighting issue: add an HDRI. Also check that Base Color is not too dark.
2. **Using dark Base Color.** Metals have bright F0 values. Color should be roughly 0.5 to 1.0.
3. **Expecting diffuse color.** This node has no diffuse layer. If it looks wrong, that is why.
4. **Wrong color space.** Color maps use *sRGB*; Roughness, Normal, and Bump maps must be **Non-Color**.
5. **Anisotropy has no effect.** Check Anisotropy is above 0, and that Rotation or Tangent are set sensibly.
6. **Overusing Roughness 0.** A perfect mirror shows every flaw and looks fake. Add subtle roughness variation (0.02 to 0.1) with a texture.
7. **Physical Conductor looks wrong.** Make sure n and k use correct RGB values (not typical 0 to 1 color values; k can exceed 1).
8. **Thin Film has no effect.** Thickness is 0 nm by default. Set it to roughly 100 to 1000 nm.
9. **Edge Tint too strong.** Subtle changes go a long way; large tints look cartoonish.

---

## 15. Quick Reference Table

| Section | Input | Type | Your Value | Purpose |
|---|---|---|---|---|
| Dropdown | Distribution | Enum | Multiscatter GGX | Microfacet model |
| Dropdown | Fresnel Type | Enum | F82 Tint | How metal color is defined |
| F82 Tint | Base Color | Color | Light warm grey | Head-on reflection color (F0) |
| F82 Tint | Edge Tint | Color | Light blue-white | Glancing-angle color (F82) |
| Physical Conductor | IOR (n) | Vector | (not shown) | Real refractive index per channel |
| Physical Conductor | Extinction (k) | Vector | (not shown) | Absorption per channel |
| Shared | Roughness | Float | 0.5 | Reflection blur |
| Shared | Anisotropy | Float | 0.0 | Stretched highlights |
| Shared | Rotation | Float | 0.0 | Stretch direction |
| Shared | Normal | Vector | none | Surface detail |
| Shared | Tangent | Vector | none | Custom anisotropy direction |
| Thin Film | Thickness | Float | 0 nm | Rainbow film thickness |
| Thin Film | IOR | Float | 1.33 | Film refraction |

---

### Summary of Your Current Setup

Your node is the **default Metallic BSDF**: a medium-rough (0.5), isotropic, grey-silver metal using **Multiscatter GGX** and the artist-friendly **F82 Tint** Fresnel model, with **Thin Film switched off** (0 nm). Raise Thickness for a rainbow tint, raise Anisotropy for brushed metal, or switch to **Physical Conductor** when you want exact, real-world metal colors.
