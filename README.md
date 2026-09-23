# noel-service
marketing website
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Noel Service | We Grow Brands</title>

  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: Arial, sans-serif;
      background: #f5f7fa;
      color: #222;
      line-height: 1.6;
    }

    header {
      background: #111;
      color: white;
      padding: 20px;
      text-align: center;
    }

    header h1 {
      font-size: 30px;
    }

    header p {
      margin-top: 5px;
      color: #ccc;
    }

    nav {
      margin-top: 15px;
    }

    nav a {
      color: white;
      text-decoration: none;
      margin: 0 10px;
    }

    .hero {
      min-height: 500px;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 40px 20px;
      background: white;
    }

    .hero h2 {
      font-size: 48px;
      margin-bottom: 15px;
    }

    .hero p {
      font-size: 20px;
      color: #666;
      margin-bottom: 25px;
    }

    .button {
      display: inline-block;
      background: #111;
      color: white;
      padding: 14px 25px;
      border-radius: 6px;
      text-decoration: none;
    }

    .section {
      padding: 60px 20px;
      max-width: 1100px;
      margin: auto;
      text-align: center;
    }

    .section h2 {
      font-size: 32px;
      margin-bottom: 30px;
    }

    .services {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 20px;
    }

    .card {
      background: white;
      padding: 30px 20px;
      border-radius: 10px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }

    .card h3 {
      margin-bottom: 10px;
    }

    .contact {
      background: #111;
      color: white;
    }

    .contact p {
      margin: 10px 0;
    }

    footer {
      background: #000;
      color: #aaa;
      text-align: center;
      padding: 20px;
    }

    @media (max-width: 600px) {
      .hero h2 {
        font-size: 36px;
      }

      nav a {
        display: inline-block;
        margin: 5px;
      }
    }
  </style>
</head>

<body>

  <header>
    <h1>Noel Service</h1>
    <p>We Grow Brands</p>

    <nav>
      <a href="#home">Home</a>
      <a href="#services">Services</a>
      <a href="#about">About</a>
      <a href="#contact">Contact</a>
    </nav>
  </header>

  <section class="hero" id="home">
    <div>
      <h2>We Grow Brands</h2>
      <p>Helping businesses get noticed, connect with customers and grow online.</p>
      <a href="#contact" class="button">Work With Us</a>
    </div>
  </section>

  <section class="section" id="services">
    <h2>Our Services</h2>

    <div class="services">

      <div class="card">
        <h3>Social Media Marketing</h3>
        <p>We help businesses build their presence and reach more people online.</p>
      </div>

      <div class="card">
        <h3>Content Creation</h3>
        <p>We create engaging content that helps brands communicate with their audience.</p>
      </div>

      <div class="card">
        <h3>Brand Promotion</h3>
        <p>We promote businesses and products to help them reach potential customers.</p>
      </div>

      <div class="card">
        <h3>Digital Marketing</h3>
        <p>We develop simple digital strategies designed to help businesses grow.</p>
      </div>

    </div>
  </section>

  <section class="section" id="about">
    <h2>About Noel Service</h2>
    <p>
      Noel Service is a marketing service focused on helping businesses
      build their brands, reach more customers and grow their online presence.
    </p>
  </section>

  <section class="section contact" id="contact">
    <h2>Let's Work Together</h2>
    <p>Ready to grow your brand?</p>
    <p>Email: noelservice@example.com</p>
    <a href="mailto:noelservice@example.com" class="button">Contact Us</a>
  </section>

  <footer>
    <p>&copy; 2026 Noel Service. All rights reserved.</p>
  </footer>

</body>
</html>
