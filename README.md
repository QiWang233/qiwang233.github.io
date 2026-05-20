# qiwang233.github.io

Personal academic homepage built with GitHub Pages.

## Structure

- `_config.yml`: site metadata
- `index.md`: homepage content
- `_layouts/homepage.html`: page layout
- `_includes/projects.md`: selected publications
- `_includes/visitors.md`: visitor map widget
- `assets/css/style.scss`: custom styles

## Development

GitHub Pages builds this site automatically from the `main` branch.

For local preview with Jekyll:

```bash
bundle exec jekyll serve
```

Then open `http://localhost:4000`.

To enable the live visitor map, add your ClustrMaps widget id to `visitor_map.clustrmaps_id` in `_config.yml`.
