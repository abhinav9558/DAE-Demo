# Portfolio Theme Showcase

A collection of professional portfolio themes designed for GitHub Pages deployment. Perfect for students and developers who want to quickly set up a beautiful portfolio website.

## 🎨 Available Themes

### Theme 1 - Professional
- **URL**: `/theme1/`
- **Style**: Clean, modern design with professional layout
- **Features**: Light theme, minimal design, excellent readability
- **Best for**: Academic portfolios, professional presentations, technical documentation

### Theme 2 - Cyberpunk
- **URL**: `/theme2/`
- **Style**: Dark, futuristic design with neon accents
- **Features**: Cyberpunk aesthetic, animated elements, striking visuals
- **Best for**: Cybersecurity professionals, tech enthusiasts, creative portfolios

## 🚀 Quick Start

### For Students/Users:
1. **Preview** themes by visiting the live demo links
2. **Download** the theme folder you prefer
3. **Upload** to your GitHub repository
4. **Enable** GitHub Pages in repository settings
5. **Deploy** and share your portfolio!

### For Developers:
1. Fork this repository
2. Customize the themes in `theme1/` and `theme2/` folders
3. Update the showcase page content
4. Deploy to GitHub Pages

## 📁 Repository Structure

```
docs/
├── _config.yml          # Main showcase site configuration
├── _data/
│   └── navigation.yml    # Showcase site navigation
├── index.md             # Theme showcase landing page
├── README.md            # This documentation
├── assets/              # Shared assets (logos, etc.)
├── theme1/              # Complete Theme 1 portfolio
│   ├── _config.yml      # Theme 1 Jekyll config
│   ├── _data/           # Theme 1 navigation
│   ├── index.md         # Theme 1 home page
│   ├── about.md         # Theme 1 about page
│   ├── projects.md      # Theme 1 projects page
│   ├── resume.md        # Theme 1 resume page
│   ├── contact.md       # Theme 1 contact page
│   └── assets/          # Theme 1 specific assets
└── theme2/              # Complete Theme 2 portfolio
    ├── _config.yml      # Theme 2 Jekyll config
    ├── _data/           # Theme 2 navigation
    ├── index.md         # Theme 2 home page
    ├── about.md         # Theme 2 about page
    ├── projects.md      # Theme 2 projects page
    ├── resume.md        # Theme 2 resume page
    ├── contact.md       # Theme 2 contact page
    └── assets/          # Theme 2 specific assets
```

## 🔧 How It Works

1. **Main Showcase Site**: The root `/docs` folder contains a Jekyll site that showcases available themes
2. **Individual Theme Sites**: Each theme folder (`theme1/`, `theme2/`) contains a complete, standalone Jekyll portfolio
3. **GitHub Pages Deployment**: The main site deploys to the root URL, with themes accessible via subdirectories
4. **Self-Contained Themes**: Each theme includes all necessary files for independent deployment

## 🛠️ Technical Details

- **Jekyll**: Static site generator with GitHub Pages support
- **Minimal Mistakes**: Base theme framework for consistency
- **Responsive Design**: All themes work perfectly on mobile and desktop
- **SEO Optimized**: Proper meta tags and structured data
- **Fast Loading**: Optimized assets and minimal dependencies

## 📝 Customizing Themes

### To Modify Existing Themes:
1. Navigate to the theme folder (`theme1/` or `theme2/`)
2. Edit the content files (`.md` files)
3. Update `_config.yml` with your information
4. Modify `_data/navigation.yml` for menu changes
5. Replace images in the `assets/` folder

### To Add New Themes:
1. Create a new folder (e.g., `theme3/`)
2. Copy the structure from an existing theme
3. Customize the design and content
4. Update the main showcase page to include the new theme

## 🔄 Local Development

### Testing the Showcase Site:
```bash
cd docs
gem install github-pages
jekyll serve
```
Visit: `http://localhost:4000/DAE-Demo/`

### Testing Individual Themes:
```bash
cd docs/theme1  # or theme2
gem install github-pages
jekyll serve
```
Visit: `http://localhost:4000/DAE-Demo/`

## 🎯 Use Cases

- **Educational Institutions**: Provide students with ready-to-use portfolio templates
- **Bootcamps**: Give graduates professional portfolio options
- **Developers**: Showcase different design approaches
- **Recruiters**: Help candidates present their work professionally

## 📄 What's Included in Each Theme

- ✅ **Complete Portfolio Pages**: Home, About, Projects, Resume, Contact
- ✅ **Responsive Design**: Works on all devices
- ✅ **SEO Optimized**: Search engine friendly
- ✅ **GitHub Pages Ready**: No setup required
- ✅ **Professional Styling**: Industry-standard designs
- ✅ **Easy Customization**: Simple content updates

## 🤝 Contributing

We welcome contributions! Please:
1. Fork the repository
2. Create a new theme or improve existing ones
3. Test thoroughly
4. Submit a pull request with clear documentation

## 📞 Support

For questions or issues:
- Check the [GitHub Issues](https://github.com/your-username/DAE-Demo/issues)
- Review the documentation
- Contact the maintainers

---

**Ready to get started?** [Choose a theme](/) and start building your professional portfolio today!