Here's the updated README without the Nodemailer section and with a more detailed breakdown of the technologies used:

---

# Prispy - Smart Retail Application

**Team:** HELLO WORLD

**Team Members:**
1. Member 1 - Reg. No: XXXX
2. Member 2 - Reg. No: XXXX
3. Member 3 - Reg. No: XXXX
4. Member 4 - Reg. No: XXXX
5. Member 5 - Reg. No: XXXX

## Project Description

### Introduction
Prispy is a smart retail application designed to automate the tracking of product details from e-commerce sites, specifically Amazon. The app helps users keep track of product prices and availability, making online shopping more efficient.

### Problem Statement
Consumers often face challenges in manually tracking product details and prices on e-commerce platforms, which can be time-consuming and prone to missed opportunities for better deals. An automated solution can streamline this process, providing real-time information and reducing manual effort.

### Solution
Prispy addresses this problem by:
- Utilizing web scraping techniques to collect data from Amazon.
- Providing a simple user interface for easy interaction with the scraped data.

### Key Features
- **Web Scraping:** Efficiently gathers data using Cheerio and Bright Data.
- **Real-Time Tracking:** Continuously monitors product information.
- **User-Friendly Interface:** Allows easy navigation and interaction with the application.

## Technologies Used

### Frontend
- **React:** A JavaScript library for building user interfaces.
- **Next.js:** A React framework for server-side rendering and generating static websites.
- **Tailwind CSS:** A utility-first CSS framework for styling.

### Backend
- **Node.js:** A JavaScript runtime built on Chrome's V8 engine for server-side development.
- **Express:** A web application framework for Node.js.

### APIs & Web Scraping
- **Cheerio:** A fast, flexible, and lean implementation of core jQuery for server-side web scraping.
- **Bright Data:** A reliable provider for web scraping and data collection services.

### Database
- **MongoDB:** A NoSQL database for storing scraped product data.

## Setup Instructions
1. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```
2. Run the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```
3. Open [http://localhost:3000](http://localhost:3000) in your browser to view the application.

## Usage Instructions
1. Input an Amazon product link in the provided field and click "Search."
2. The application will scrape the product details and display them in the cart below.
3. **Note:** Ensure that the link is from the Amazon website. The application currently supports only Amazon, and there may be instances where data retrieval is inconsistent due to the nature of web scraping.
4. Click on a product card to view detailed information about the product.

## Theme Fit
**Smart Retail:** Prispy enhances the online shopping experience by providing a smart solution for tracking product details and prices on e-commerce sites. By automating this process, it saves users time and ensures they are informed about product updates, aligning with the "Smart Retail" theme by optimizing and modernizing retail practices.

## Future Enhancements
- Expand tracking capabilities to include other e-commerce sites.
- Improve the user interface for better user engagement.
- Optimize the efficiency and speed of the web scraping process.

---

Feel free to reach out to me at: https://github.com/drave-coding to get a better insight of the app. Always open to feedback and critics.