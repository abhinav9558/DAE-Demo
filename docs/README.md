# Alex Rivera Portfolio - Dual Theme Setup

This portfolio website features a unique dual-theme experience that allows visitors to choose between two different visual styles while maintaining the same content.

## 🎨 Theme Options

### Light Theme (`/light/`)
- Clean, professional design
- Bright, modern aesthetic
- Perfect for showcasing technical content
- Uses minimal-mistakes "default" skin

### Dark Theme (`/dark/`)
- Cyberpunk-inspired design
- Dark background with neon accents
- Perfect for cybersecurity aesthetic
- Custom CSS with neon color scheme

## 🚀 GitHub Pages Deployment

This setup is designed to work seamlessly with GitHub Pages using a single deployment:

### File Structure
```
docs/
├── _config.yml          # Main site configuration
├── _data/
│   └── navigation.yml   # Main navigation with theme selector
├── assets/              # Shared images and CSS
├── index.md             # Theme selector landing page
├── light.md             # Light theme homepage
├── dark.md              # Dark theme homepage
├── about.md             # Shared content pages
├── projects.md
├── resume.md
├── contact.md
├── theme1/              # Original light theme files (excluded from build)
└── theme2/              # Original dark theme files (excluded from build)
```

### How It Works

1. **Main Landing Page**: Visitors first see a theme selector at `/`
2. **Theme Selection**: Users can choose between light (`/light/`) or dark (`/dark/`) themes
3. **Shared Content**: All content pages (about, projects, resume, contact) are shared between themes
4. **Single Deployment**: Everything runs from one GitHub Pages site

### Deployment Steps

1. **Repository Setup**:
   ```bash
   # Your repository should be named: username.github.io or any-repo-name
   # Enable GitHub Pages in repository settings
   # Set source to "Deploy from a branch" and select "main" branch, "/docs" folder
   ```

2. **Configuration**:
   - Update `_config.yml` with your GitHub username and repository name
   - Update URLs in navigation and content files
   - Replace placeholder images in `/assets/img/`

3. **Customization**:
   - Modify content in the shared `.md` files
   - Adjust styling in `dark.md` for the dark theme
   - Update author information and links

## 🛠️ Technical Implementation

### Theme Switching
- Uses Jekyll's minimal-mistakes theme as the base
- Light theme uses the default skin
- Dark theme uses custom CSS variables for neon effects
- Both themes share the same content and navigation structure

### SEO & Performance
- Single site means better SEO consolidation
- Shared assets reduce load times
- Proper meta tags and structured data
- Mobile-responsive design for both themes

### Maintenance
- Update content once in shared files
- Both themes automatically reflect changes
- Easy to add new pages or modify existing ones

## 📝 Content Management

To update content:
1. Edit the shared `.md` files in the root directory
2. Changes will appear on both theme versions
3. Theme-specific styling is handled in the respective theme pages

## 🔧 Local Development

For local development, GitHub Pages uses Jekyll automatically. Simply push your changes to the repository and GitHub Pages will build and deploy your site.

If you want to test locally, you can use GitHub's recommended approach:
```bash
# Install GitHub Pages gem (optional for local testing)
gem install github-pages

# Serve locally (optional)
jekyll serve

# Visit http://localhost:4000
```

## 📱 Features

- **Responsive Design**: Works on all devices
- **Fast Loading**: Optimized assets and minimal dependencies
- **SEO Optimized**: Proper meta tags and structured data
- **Accessible**: WCAG compliant design
- **GitHub Pages Compatible**: No custom plugins required

---

*This dual-theme approach provides a unique user experience while maintaining the simplicity of a single GitHub Pages deployment.*