# GitHub Pages Deployment Guide

This guide will help you deploy the Portfolio Theme Showcase to GitHub Pages.

## 🚀 Quick Deployment

### Step 1: Repository Setup
1. Fork or clone this repository
2. Ensure your repository is public (required for free GitHub Pages)
3. Navigate to your repository on GitHub

### Step 2: Enable GitHub Pages
1. Go to **Settings** → **Pages** in your repository
2. Under **Source**, select "Deploy from a branch"
3. Choose **Branch**: `main` (or your default branch)
4. Choose **Folder**: `/docs`
5. Click **Save**

### Step 3: Configure Your Site
1. Edit `docs/_config.yml`:
   ```yaml
   url: "https://YOUR-USERNAME.github.io"
   baseurl: "/YOUR-REPOSITORY-NAME"
   ```
2. Update the GitHub links in `docs/index.md` and `docs/README.md`
3. Replace any placeholder content with your information

### Step 4: Wait for Deployment
- GitHub Pages typically takes 2-10 minutes to deploy
- Check the **Actions** tab for build status
- Your site will be available at: `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY-NAME/`

## 🎨 Accessing Individual Themes

Once deployed, your themes will be accessible at:
- **Main Showcase**: `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY-NAME/`
- **Theme 1**: `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY-NAME/theme1/`
- **Theme 2**: `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY-NAME/theme2/`

## 📝 Customizing Themes

### For Students Using a Theme:
1. **Download** the theme folder you want (`theme1/` or `theme2/`)
2. **Create** a new repository named `YOUR-USERNAME.github.io`
3. **Upload** the theme files to the root of your repository
4. **Edit** the content files with your information:
   - `_config.yml` - Site configuration and personal info
   - `index.md` - Homepage content
   - `about.md` - About page
   - `projects.md` - Your projects
   - `resume.md` - Your resume/CV
   - `contact.md` - Contact information
5. **Replace** images in the `assets/img/` folder
6. **Enable** GitHub Pages (source: root directory)

### For Developers Adding New Themes:
1. **Create** a new folder (e.g., `theme3/`)
2. **Copy** the structure from an existing theme
3. **Customize** the design and content
4. **Update** the main showcase page (`index.md`) to include the new theme
5. **Test** locally before deploying

## 🔧 Local Development

### Prerequisites
- Ruby 2.7+ (recommended)
- Bundler gem

### Setup
```bash
# Navigate to the docs directory
cd docs

# Install dependencies
bundle install

# Serve the site locally
bundle exec jekyll serve

# Visit http://localhost:4000/YOUR-REPOSITORY-NAME/
```

### Testing Individual Themes
```bash
# Test Theme 1
cd docs/theme1
bundle install
bundle exec jekyll serve

# Test Theme 2
cd docs/theme2
bundle install
bundle exec jekyll serve
```

## 🐛 Troubleshooting

### Common Issues

**Site not loading after deployment:**
- Check that GitHub Pages is enabled in repository settings
- Verify the `url` and `baseurl` in `_config.yml`
- Ensure the repository is public
- Check the Actions tab for build errors

**Themes not accessible:**
- Verify that `theme1/` and `theme2/` folders contain `_config.yml` files
- Check that the folder structure is correct
- Ensure all theme files are committed to the repository

**Local development issues:**
- Update Ruby to version 2.7 or higher
- Run `bundle update` to update dependencies
- Clear Jekyll cache: `bundle exec jekyll clean`

**Images not displaying:**
- Check image paths in markdown files
- Ensure images are in the correct `assets/img/` directory
- Verify image file names match exactly (case-sensitive)

### Build Errors
If you encounter build errors:
1. Check the **Actions** tab in your GitHub repository
2. Review the build logs for specific error messages
3. Common fixes:
   - Fix YAML syntax errors in `_config.yml`
   - Remove or fix invalid markdown syntax
   - Ensure all required files are present

## 📞 Support

If you need help:
1. Check this deployment guide
2. Review the main [README.md](README.md)
3. Check [GitHub Issues](https://github.com/your-username/DAE-Demo/issues)
4. Create a new issue with:
   - Your repository URL
   - Error messages (if any)
   - Steps you've already tried

## ✅ Deployment Checklist

- [ ] Repository is public
- [ ] GitHub Pages is enabled
- [ ] `_config.yml` has correct URL and baseurl
- [ ] All theme folders contain necessary files
- [ ] Personal information is updated
- [ ] Images are uploaded and paths are correct
- [ ] Site builds successfully (check Actions tab)
- [ ] All theme links work correctly

---

**Ready to deploy?** Follow the steps above and your portfolio theme showcase will be live in minutes!