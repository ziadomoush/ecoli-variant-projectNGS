# E. coli Variant Analysis Website

English project documentation prepared for Ziad. Open `index.html` after extracting the package.

## What is included

- Sidebar navigation with 26 page views, including 17 illustrated workflow steps.
- Interactive work pipeline; color-highlighted Bash commands; code explanations and copy buttons.
- Verified results, original IGV evidence with zoom, two annotation summaries.
- The complete readable report, the English PDF and the presentation.
- Actual original VCF and report files, one individual FastQC report, and the combined MultiQC HTML.
- Local Cairo font files; no build tools or online font dependencies.

## Add the remaining original project files

The documentation is complete for the performed workflow. The downloadable data collection is intentionally explicit about files not present in this package: BAM/BAI, reference/indexes, FASTQ inputs and five individual FastQC reports. This does not mean the analysis was not performed. It means those bytes must be copied from the original project folder if visitors should download them.

Copy original files into the same `data/`, `results/` and `reports/` relative paths. Open Project files to see expected filenames. From inside the website directory, run:

```bash
python3 scripts/refresh_manifest.py
python3 scripts/check_site.py
```

The updater runs only on your computer and refreshes the included-file inventory. It does not analyze sequencing data. Re-upload the updated `assets/manifest.js` and `assets/file-manifest.json`, plus newly added files. Keep the HTML file and assets directory together.

The Project files page also has a local folder-mapping feature for checking your files privately in your browser. Local folder mapping is temporary and does not upload them for visitors. On the hosted site, Check uploaded files tests previously absent expected paths.

## Publish on GitHub Pages

1. Create a repository and upload the extracted website contents, with `index.html` at the repository root. Do not upload only the ZIP.
2. Open Settings > Pages > Deploy from a branch.
3. Choose main and /(root), then Save.
4. Open the URL GitHub provides and test the report, QC, VCF downloads and images.

GitHub browser upload limit: 25 MiB per file. Regular Git blocks files over 100 MiB. Final BAM files can exceed the browser limit; large SAM intermediates should not be needed for the documentation. An LFS pointer is not a directly usable scientific file on a static page.

Official instructions:
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github

## Scientific scope

The original inputs were pretrimmed, subsampled reads. No second Trimmomatic step was run. Variant calling used a haploid model and the retained call sets used QUAL >= 30, FORMAT/DP >= 5 and nonmissing genotypes. Counts are 22/710/8. Gene annotation and manual coding-effect predictions cover the six shared variants only. SnpEff was not run. The 43,944-base zero-depth interval is not a confirmed deletion junction. Generated conceptual art is labeled and is not used as experimental evidence.

The site is documentation, not an analysis execution service. Original command examples may overwrite matching outputs if rerun. The original analysis folders should be preserved separately.
