# corrbuilders.co.uk

Static website bundle for `corrbuilders.co.uk`.

## Current structure

- `index.html`: site entrypoint
- `netlify.toml`: Netlify publishing, redirect, and header configuration
- `scripts/validate_site.py`: local and CI validation for the static bundle

## Local validation

Run:

```bash
python3 scripts/validate_site.py
```

## GitHub pipeline

The GitHub Actions workflow at `.github/workflows/ci.yml` runs on pushes and pull requests. It:

- validates that the required site files exist
- checks key metadata and Netlify configuration
- creates a deploy artifact containing `index.html` and `netlify.toml`

## Deployment

This repository is structured for Netlify static hosting with the site root published from the repository root.
