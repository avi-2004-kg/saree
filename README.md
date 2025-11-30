# Kumudhini Silks Website

A responsive website for Kumudhini Silks, a luxury saree boutique in Bengaluru specializing in Kancheepuram and Banarasi silks.

## Features

- Responsive design that works on all devices
- Modern UI with elegant color scheme reflecting the brand
- Complete website with Home, About, Products, Catalogue, and Contact pages
- Contact form with backend processing
- SEO-friendly structure with proper meta tags

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python Flask
- **Fonts**: Google Fonts (Playfair Display, Raleway)

## Setup Instructions

1. **Clone the repository**
   ```
   git clone <repository-url>
   cd sussu
   ```

2. **Create a virtual environment**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```
   python app.py
   ```

6. **Access the website**
   Open your browser and go to `http://127.0.0.1:5000`

## Project Structure

```
sussu/
│
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
│
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── about.html        # About page
│   ├── products.html     # Products page
│   ├── catalogue.html    # Catalogue page
│   └── contact.html      # Contact page
│
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Main stylesheet
│   └── js/
│       └── script.js     # JavaScript file
```

## Customization

To customize the website:

1. **Content**: Edit the HTML files in the `templates/` directory
2. **Styling**: Modify `static/css/style.css`
3. **Scripts**: Update `static/js/script.js`
4. **Backend**: Modify `app.py` for additional functionality

## Deployment

For production deployment, consider using:

- Gunicorn or uWSGI as a WSGI server
- Nginx as a reverse proxy
- A cloud platform like Heroku, AWS, or DigitalOcean

## License

This project is proprietary to Kumudhini Silks and should not be distributed without permission.