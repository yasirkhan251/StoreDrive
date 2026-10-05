<h1 align="center">☁️ StoreDrive</h1>

<p align="center">
  <strong>A Django-based personal media storage, management and streaming platform</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
</p>

---

<h2>🎯 What This Project Offers</h2>

<p>
<strong>StoreDrive</strong> is a personal cloud-style media management application
built with Django. It provides authenticated users with a private dashboard where
they can organize and manage different types of media from one interface.
</p>

<p>
The application separates user data and provides dedicated interfaces for
<strong>photos, music, videos and movies</strong>, along with profile management,
password recovery and browser-based media playback.
</p>

---

<h2>✨ Highlighted Features</h2>

<table>
<tr>

<td width="33%" align="center" valign="top">

<h3>🔐 Authentication</h3>

<p>
User registration, login, logout and session-based authentication.
</p>

</td>

<td width="33%" align="center" valign="top">

<h3>🔑 Password Recovery</h3>

<p>
Email-based verification code workflow for resetting passwords.
</p>

</td>

<td width="33%" align="center" valign="top">

<h3>👤 User Profiles</h3>

<p>
Profile information, profile image management and account settings.
</p>

</td>

</tr>

<tr>

<td width="33%" align="center" valign="top">

<h3>🖼️ Photo Library</h3>

<p>
Upload, browse, search and manage personal photos.
</p>

</td>

<td width="33%" align="center" valign="top">

<h3>🎵 Music Library</h3>

<p>
Upload and play music directly from the browser with custom playback controls.
</p>

</td>

<td width="33%" align="center" valign="top">

<h3>🎬 Video Library</h3>

<p>
Upload videos and watch them through a custom browser player.
</p>

</td>

</tr>

<tr>

<td width="33%" align="center" valign="top">

<h3>🍿 Movie Library</h3>

<p>
Store movies separately with dedicated viewing pages.
</p>

</td>

<td width="33%" align="center" valign="top">

<h3>📊 Dashboard</h3>

<p>
See totals for files, photos, music, videos and movies at a glance.
</p>

</td>

<td width="33%" align="center" valign="top">

<h3>🗑️ File Management</h3>

<p>
Delete media and remove associated stored files.
</p>

</td>

</tr>
</table>

---

<h2>🧠 How It Works</h2>

<pre>
                    StoreDrive
                         │
                         ▼
                ┌────────────────┐
                │ Authentication │
                └───────┬────────┘
                        │
                        ▼
                 ┌─────────────┐
                 │  Dashboard  │
                 └──────┬──────┘
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
   ┌────────┐      ┌──────────┐     ┌──────────┐
   │ Photos │      │  Music   │     │  Videos  │
   └────────┘      └──────────┘     └──────────┘
                                          │
                                          ▼
                                    ┌──────────┐
                                    │  Movies  │
                                    └──────────┘

                        │
                        ▼

               User Profile / Settings
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
       Profile Update        Password Change
</pre>

<p>
Every media record is associated with the authenticated user, allowing the
application to query and display each user's own library.
</p>

---

<h2>🏗️ Application Architecture</h2>

<table>
<tr>
<th>Component</th>
<th>Responsibility</th>
</tr>

<tr>
<td><code>Accounts</code></td>
<td>User authentication, custom user model, signup, login and account-related workflows.</td>
</tr>

<tr>
<td><code>DataBase</code></td>
<td>Media models, uploads, media views, deletion and streaming functionality.</td>
</tr>

<tr>
<td><code>StoreDrive</code></td>
<td>Main Django project configuration, URLs, password recovery and shared views.</td>
</tr>

<tr>
<td><code>templates</code></td>
<td>Server-rendered user interface using Django templates.</td>
</tr>

<tr>
<td><code>static</code></td>
<td>CSS, JavaScript, icons, images and media-player assets.</td>
</tr>

<tr>
<td><code>media</code></td>
<td>User-uploaded files and profile images.</td>
</tr>
</table>

---

<h2>🛠️ Software & Technologies Used</h2>

<table>
<tr>
<th>Technology</th>
<th>Role</th>
</tr>

<tr>
<td>🐍 Python</td>
<td>Primary programming language</td>
</tr>

<tr>
<td>🌐 Django</td>
<td>Web framework and application backend</td>
</tr>

<tr>
<td>🗄️ SQLite</td>
<td>Development database</td>
</tr>

<tr>
<td>🖥️ Django Templates</td>
<td>Server-side HTML rendering</td>
</tr>

<tr>
<td>🎨 HTML / CSS</td>
<td>User interface and styling</td>
</tr>

<tr>
<td>⚡ JavaScript</td>
<td>Interactive frontend behavior and media controls</td>
</tr>

<tr>
<td>🖼️ Pillow</td>
<td>Image processing and profile-image cropping</td>
</tr>

<tr>
<td>🎵 Mutagen</td>
<td>MP3 metadata and embedded artwork handling</td>
</tr>

<tr>
<td>📧 SMTP / Gmail</td>
<td>Password-reset verification email delivery</td>
</tr>
</table>

---

<h2>💻 System Requirements</h2>

<ul>
<li>Windows, Linux or macOS</li>
<li>Python 3.x</li>
<li>pip</li>
<li>Git</li>
<li>Modern web browser</li>
<li>Enough disk space for uploaded media</li>
</ul>

<p>
Because StoreDrive is a media-storage application, required storage capacity
depends heavily on the number and size of uploaded photos, music files,
videos and movies.
</p>

---

<h2>📦 Installation & Setup</h2>

<h3>1️⃣ Clone the Repository</h3>

```bash
git clone https://github.com/yasirkhan251/StoreDrive.git
cd StoreDrive
```

<h3>2️⃣ Create a Virtual Environment</h3>

```bash
python -m venv venv
```

<p>Windows:</p>

```bash
venv\Scripts\activate
```

<p>Linux / macOS:</p>

```bash
source venv/bin/activate
```

<h3>3️⃣ Install Dependencies</h3>

<p>
The repository currently does not contain a <code>requirements.txt</code>.
Install Django and the libraries used by the project:
</p>

```bash
pip install django pillow mutagen
```

<p>
You may also want to freeze the environment after installation:
</p>

```bash
pip freeze > requirements.txt
```

---

<h2>⚙️ Database Setup</h2>

<p>
StoreDrive uses Django migrations and SQLite during development.
</p>

```bash
python manage.py makemigrations
python manage.py migrate
```

<p>
Create an administrator account:
</p>

```bash
python manage.py createsuperuser
```

---

<h2>📁 Media & Static Files</h2>

<p>
The application uses Django's media configuration for uploaded content.
The settings define:
</p>

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

<p>
Uploaded files are separated into media categories such as:
</p>

```text
media/
├── movies/
├── music/
├── photos/
├── videos/
└── profile_pics/
```

<p>
Static frontend assets are stored under the project's
<code>static/</code> directory.
</p>

---

<h2>▶️ How to Run</h2>

```bash
python manage.py runserver
```

<p>
Then open:
</p>

```text
http://127.0.0.1:8000/
```

<p>
The root URL redirects to the authentication interface.
</p>

---

<h2>🔐 Authentication Workflow</h2>

<pre>
New User
   │
   ▼
Sign Up
   │
   ▼
Account Created
   │
   ▼
Automatic Login
   │
   ▼
Dashboard
</pre>

<p>Returning users:</p>

<pre>
Username + Password
        │
        ▼
     Login
        │
        ▼
 Authentication
        │
        ▼
    Dashboard
</pre>

<h3>🔑 Forgot Password</h3>

<pre>
Username / Email
       │
       ▼
Generate Verification Code
       │
       ▼
Send Email
       │
       ▼
Enter Verification Code
       │
       ▼
Create New Password
</pre>

<p>
The verification token is stored with an expiration timestamp and is intended
to remain valid for a limited period.
</p>

---

<h2>🖼️ Photos</h2>

<p>
The photo module allows authenticated users to upload and browse images belonging
to their own account.
</p>

<p>Typical workflow:</p>

<pre>
Select Photo
     ↓
Upload
     ↓
Django FileField
     ↓
User-specific Database Record
     ↓
Photo Gallery
</pre>

---

<h2>🎵 Music</h2>

<p>
The music module provides browser-based playback for uploaded audio files.
The interface includes custom JavaScript controls for playing, pausing,
seeking and repeating tracks.
</p>

<p>Supported upload extensions currently include:</p>

```text
.mp3
.m4a
```

<p>
The project also uses <strong>Mutagen</strong> for MP3-related metadata and
embedded artwork processing.
</p>

---

<h2>🎬 Videos</h2>

<p>
Videos can be uploaded to the user's personal library and opened through a
dedicated video landing page.
</p>

<p>Current upload extensions include:</p>

```text
.mp4
.mkv
.avi
.3gp
```

---

<h2>🍿 Movies</h2>

<p>
Movies have a separate model and interface from ordinary videos. Each movie
can have a title and uploaded media file and is opened through its own
watch page.
</p>

<p>Current upload extensions include:</p>

```text
.mp4
.3gp
.mkv
.avi
.webm
```

---

<h2>▶️ Custom Media Player</h2>

<p>
StoreDrive includes a custom browser-based video player rather than relying
solely on the browser's default controls.
</p>

<p>The player UI includes:</p>

<ul>
<li>▶️ Play / pause</li>
<li>🔊 Volume controls</li>
<li>🔇 Mute</li>
<li>⏱️ Timeline and seeking</li>
<li>⚡ Playback speed</li>
<li>🖥️ Theater mode</li>
<li>📺 Full-screen mode</li>
<li>🎬 Dedicated viewing pages</li>
</ul>

---

<h2>👤 User Profile & Settings</h2>

<p>
Authenticated users can access their own profile and settings area.
</p>

<ul>
<li>👤 View profile information</li>
<li>🖼️ Upload a profile image</li>
<li>✏️ Update profile information</li>
<li>🔑 Change password</li>
<li>📧 View account email</li>
<li>🆔 View generated server ID</li>
<li>🗑️ Delete the account</li>
</ul>

<p>
Profile images are processed with Pillow and cropped to a square format before
being stored.
</p>

---

<h2>📊 Dashboard</h2>

<p>
The dashboard provides a quick overview of the user's media collection.
</p>

<table>
<tr>
<th>Category</th>
<th>Displayed Information</th>
</tr>

<tr>
<td>📁 Files</td>
<td>Total stored media records</td>
</tr>

<tr>
<td>🖼️ Photos</td>
<td>Total photos</td>
</tr>

<tr>
<td>🎵 Music</td>
<td>Total music records</td>
</tr>

<tr>
<td>🎬 Movies</td>
<td>Total movies</td>
</tr>

<tr>
<td>🎥 Videos</td>
<td>Total videos</td>
</tr>
</table>

---

<h2>📂 Project Structure</h2>

```text
StoreDrive/
│
├── Accounts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── migrations/
│
├── DataBase/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── utils.py
│   ├── admin.py
│   └── migrations/
│
├── StoreDrive/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
│   └── asgi.py
│
├── templates/
│   ├── authentication.html
│   ├── dashboard.html
│   ├── files.html
│   ├── photos.html
│   ├── music.html
│   ├── videos.html
│   ├── movies.html
│   ├── profile.html
│   ├── settings.html
│   └── landingpages/
│
├── static/
│   ├── authentication/
│   ├── landing/
│   ├── media/
│   └── data/
│
├── media/
├── manage.py
└── db.sqlite3
```

---

<h2>🧩 Main Data Models</h2>

<table>
<tr>
<th>Model</th>
<th>Purpose</th>
</tr>

<tr>
<td><code>MyUser</code></td>
<td>Custom authenticated user with profile information.</td>
</tr>

<tr>
<td><code>Forgotpassword</code></td>
<td>Stores password-recovery verification data.</td>
</tr>

<tr>
<td><code>Photos</code></td>
<td>Stores user photo records.</td>
</tr>

<tr>
<td><code>Music</code></td>
<td>Stores user audio records.</td>
</tr>

<tr>
<td><code>Videos</code></td>
<td>Stores user video records.</td>
</tr>

<tr>
<td><code>Movies</code></td>
<td>Stores user movie records.</td>
</tr>
</table>

<p>
Each media model is linked to <code>MyUser</code>, which allows the application
to retrieve media for the currently authenticated user.
</p>

---

<h2>🖼️ Screenshots & Demo</h2>

<p>
Add screenshots to a dedicated documentation directory such as:
</p>

```text
docs/
└── images/
    ├── login.png
    ├── signup.png
    ├── dashboard.png
    ├── photos.png
    ├── music.png
    ├── videos.png
    ├── movies.png
    ├── profile.png
    └── settings.png
```

<p align="center">
  <img src="docs/images/dashboard.png" width="850" alt="StoreDrive Dashboard">
</p>

<p align="center">
  <em>📊 StoreDrive dashboard</em>
</p>

<h3>🎞️ GIF Demonstrations</h3>

<p align="center">
  <img src="docs/demo/upload-demo.gif" width="850" alt="StoreDrive Upload Demo">
</p>

<h3>🎥 Video Demonstration</h3>

<p align="center">
  <a href="YOUR-YOUTUBE-VIDEO-LINK">
    <img src="docs/images/video-thumbnail.png" width="850" alt="StoreDrive Video Demo">
  </a>
</p>

<p align="center">
  ▶️ <strong>Watch the complete StoreDrive demonstration</strong>
</p>

---

<h2>⚠️ Limitations</h2>

<ul>
<li>The project is currently configured primarily as a development application.</li>
<li>SQLite is used as the default database.</li>
<li>Uploaded media is stored locally rather than in a production cloud object-storage service.</li>
<li>Media storage capacity depends on the host machine's disk space.</li>
<li>The application should receive additional production hardening before public deployment.</li>
<li>Some UI features depend on locally served/static frontend assets.</li>
</ul>

---

<h2>🔒 Security Notes</h2>

<p>
<strong>Before deploying this repository publicly or to production, move all
credentials and secrets out of <code>settings.py</code>.</strong>
</p>

<p>
The current configuration contains sensitive values such as the Django
<code>SECRET_KEY</code> and SMTP credentials. These should be replaced and
stored using environment variables or a secret-management system.
</p>

<p>Recommended pattern:</p>

```python
import os

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
```

<p>
Do not commit real passwords, API keys or application secrets to GitHub.
</p>

---

<h2>🔮 Future Improvements / Roadmap</h2>

<table>
<tr>
<td>☁️ Cloud Storage</td>
<td>Move media storage to S3-compatible object storage.</td>
</tr>

<tr>
<td>📱 Responsive UI</td>
<td>Improve the media experience across phones and tablets.</td>
</tr>

<tr>
<td>🔍 Advanced Search</td>
<td>Add metadata-aware search and filtering.</td>
</tr>

<tr>
<td>📊 Storage Analytics</td>
<td>Show storage usage and media statistics.</td>
</tr>

<tr>
<td>🧑‍🤝‍🧑 Sharing</td>
<td>Allow users to share selected files or media.</td>
</tr>

<tr>
<td>🔒 Production Security</td>
<td>Environment-based secrets, HTTPS, secure cookies and deployment hardening.</td>
</tr>

<tr>
<td>🚀 Production Database</td>
<td>Support PostgreSQL or another production-grade database.</td>
</tr>
</table>

---

<h2>👨‍💻 Author</h2>

<p align="center">

<strong>Yasir Khan</strong><br>
Full Stack Developer • Django Developer • AI/ML Enthusiast

<br><br>

<a href="https://github.com/yasirkhan251">
  <img src="https://img.shields.io/badge/GitHub-yasirkhan251-181717?style=for-the-badge&logo=github">
</a>

<a href="https://yasirkhan.in">
  <img src="https://img.shields.io/badge/Portfolio-yasirkhan.in-0A66C2?style=for-the-badge">
</a>

</p>

---

<p align="center">
  <strong>☁️ StoreDrive — Your personal space for photos, music, videos and movies.</strong>
</p>
