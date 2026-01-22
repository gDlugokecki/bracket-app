# Design Tokens & Typography Guidelines

## Typography Scale

Use this scale consistently throughout the app. Don't use arbitrary sizes.

### Headings

| Element | Size | Weight | Usage |
|---------|------|--------|-------|
| Page Title (H1) | `text-4xl lg:text-5xl` | `font-extrabold` | Main page heading (e.g., "Tournament Details") |
| Section Title (H2) | `text-3xl` | `font-semibold` | Major sections (e.g., "Participants", "Bracket") |
| Subsection (H3) | `text-2xl` | `font-semibold` | Cards, modals, subsections |
| Small Heading (H4) | `text-xl` | `font-semibold` | Smaller sections, list headers |

### Body Text

| Usage | Classes | Example |
|-------|---------|---------|
| Body text | `text-base leading-7` | Paragraphs, descriptions |
| Large body | `text-lg` | Intro paragraphs, important text |
| Small text | `text-sm` | Captions, labels, metadata |
| Tiny text | `text-xs` | Timestamps, fine print |

### Special Text Styles

| Usage | Classes | Example |
|-------|---------|---------|
| Lead text | `text-xl text-muted-foreground` | Introduction paragraphs |
| Muted text | `text-sm text-muted-foreground` | Timestamps, secondary info |
| Error text | `text-sm text-destructive` | Error messages |
| Success text | `text-sm text-green-600` | Success messages |
| Code | `font-mono text-sm bg-muted px-1 py-0.5 rounded` | Inline code |

## Color Usage

### Text Colors

- `text-foreground` - Default text color (use for most text)
- `text-muted-foreground` - Secondary text (timestamps, captions, helper text)
- `text-primary` - Links, important actions
- `text-destructive` - Errors, warnings, delete actions
- `text-green-600` - Success messages, positive states

### When to Use Custom Colors

Only deviate from semantic colors for:
- Status indicators (match status, tournament state)
- Data visualization (charts, brackets)
- Branding elements (logo, hero sections)

## Spacing Scale

Stick to Tailwind's spacing scale (increments of 4):

- `space-y-1` (4px) - Tight groups (form labels + inputs)
- `space-y-2` (8px) - Related items
- `space-y-4` (16px) - Form fields, list items
- `space-y-6` (24px) - Sections within a card
- `space-y-8` (32px) - Major sections

## Examples

### Page Structure
```vue
<div class="p-6">
  <div class="max-w-7xl mx-auto space-y-8">
    <!-- Page title -->
    <h1 class="text-4xl font-extrabold">Dashboard</h1>

    <!-- Section -->
    <section class="space-y-4">
      <h2 class="text-2xl font-semibold">Recent Tournaments</h2>
      <p class="text-muted-foreground">Your latest tournament activity</p>
      <!-- content -->
    </section>
  </div>
</div>
```

### Card Component
```vue
<Card>
  <CardHeader>
    <h3 class="text-xl font-semibold">Tournament Name</h3>
    <p class="text-sm text-muted-foreground">Created 2 days ago</p>
  </CardHeader>
  <CardContent>
    <p class="text-base">Tournament description goes here...</p>
  </CardContent>
</Card>
```

### Form
```vue
<form class="space-y-4">
  <div class="space-y-1">
    <label class="text-sm font-medium">Tournament Name</label>
    <input />
    <p class="text-xs text-muted-foreground">Choose a unique name</p>
  </div>
</form>
```

## Rules for Consistency

1. **Never use arbitrary values** - Use Tailwind's scale (`text-[17px]` ❌, `text-lg` ✅)
2. **Stick to the semantic colors** - Don't use `text-gray-600` randomly
3. **Use the spacing scale** - `space-y-4`, `space-y-6`, `space-y-8` (no `space-y-5`)
4. **Font weights** - Use `font-medium`, `font-semibold`, `font-bold` (avoid `font-[550]`)
5. **Line height** - Use `leading-tight`, `leading-normal`, `leading-relaxed`

## When to Use Typography Component

Use `<Typography>` component for:
- ✅ Semantic HTML enforcement (`<Typography variant="h1">`)
- ✅ Common patterns (`variant="muted"`, `variant="lead"`)

Use plain HTML + Tailwind for:
- ✅ Everything else (most text)
- ✅ Custom colors
- ✅ One-off styles
