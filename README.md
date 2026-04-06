# corrbuilders.co.uk

Static website bundle for `corrbuilders.co.uk`.

## Current structure

- `index.html`: site entrypoint
- `netlify.toml`: Netlify publishing, redirect, and header configuration
- `package.json`: local development commands
- `scripts/serve_site.py`: local preview server
- `scripts/validate_site.py`: local and CI validation for the static bundle

## Local preview

Run:

```bash
npm run dev
```

Then open:

```text
http://127.0.0.1:8000
```

## Local validation

Run:

```bash
npm run validate
```

## GitHub pipeline

The GitHub Actions workflow at `.github/workflows/ci.yml` runs on pushes and pull requests. It:

- validates that the required site files exist
- checks key metadata and Netlify configuration
- creates a deploy artifact containing `index.html` and `netlify.toml`

## Deployment

This repository is structured for Netlify static hosting with the site root published from the repository root.

There is already a Netlify project for this site. The intended workflow is:

1. Run `npm run dev` and review changes locally
2. Run `npm run validate`
3. Commit and push to GitHub
4. Let Netlify deploy from the GitHub-connected repository
