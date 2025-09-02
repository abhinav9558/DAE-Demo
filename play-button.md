# Play Button Component

A modern, interactive play button component for media controls.

## Overview

This play button provides an intuitive interface for controlling media playback with smooth animations and responsive design.

## Features

- **Toggle Functionality**: Switches between play and pause states
- **Smooth Animations**: CSS transitions for state changes
- **Responsive Design**: Adapts to different screen sizes
- **Accessibility**: Keyboard navigation and screen reader support

## Mock Data

```json
{
  "playButton": {
    "id": "media-play-btn",
    "state": "paused",
    "size": "large",
    "color": "#007bff",
    "disabled": false,
    "ariaLabel": "Play media content",
    "mediaInfo": {
      "title": "Sample Audio Track",
      "duration": "3:45",
      "currentTime": "0:00",
      "volume": 0.8,
      "muted": false
    },
    "animations": {
      "hoverScale": 1.1,
      "transitionDuration": "0.3s",
      "easing": "ease-in-out"
    }
  }
}
```

## Usage Example

```html
<button 
  id="media-play-btn" 
  class="play-button" 
  aria-label="Play media content"
  data-state="paused"
>
  <svg class="play-icon" viewBox="0 0 24 24">
    <path d="M8 5v14l11-7z"/>
  </svg>
  <svg class="pause-icon" viewBox="0 0 24 24" style="display: none;">
    <path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/>
  </svg>
</button>
```

## Styling

```css
.play-button {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: #007bff;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  display: flex;
  align-items: center;
  justify-content: center;
}

.play-button:hover {
  transform: scale(1.1);
  background: #0056b3;
}

.play-button svg {
  width: 24px;
  height: 24px;
  fill: white;
}
```

## JavaScript Functionality

```javascript
const playButton = document.getElementById('media-play-btn');
let isPlaying = false;

playButton.addEventListener('click', () => {
  isPlaying = !isPlaying;
  
  if (isPlaying) {
    playButton.setAttribute('data-state', 'playing');
    playButton.setAttribute('aria-label', 'Pause media content');
    // Show pause icon, hide play icon
    playButton.querySelector('.play-icon').style.display = 'none';
    playButton.querySelector('.pause-icon').style.display = 'block';
  } else {
    playButton.setAttribute('data-state', 'paused');
    playButton.setAttribute('aria-label', 'Play media content');
    // Show play icon, hide pause icon
    playButton.querySelector('.play-icon').style.display = 'block';
    playButton.querySelector('.pause-icon').style.display = 'none';
  }
});
```

## States

- **Paused**: Default state, shows play triangle icon
- **Playing**: Active state, shows pause bars icon
- **Loading**: Shows spinner animation
- **Disabled**: Grayed out, non-interactive

## Accessibility

- ARIA labels for screen readers
- Keyboard navigation support (Space/Enter)
- High contrast mode compatibility
- Focus indicators for keyboard users