# ShopGenie-API
This AI agent , ShopGenie , is built on langGraph and aims to provide decisive shopping experience to all people using the power of LLM.It uses tavily for web search , and llama-3.1-70B-versatile model through groq. This ai agent is made using totally open source technologies.

Python 3.10.7 
mongodb 8.0.12 https://www.mongodb.com/try/download/community



GROQ API Key: # Expires within 24 hrs
1. Go to console.groq.com.
2. Sign up or log in.
3. Navigate to the "API Keys" section.
4. Create and copy your API key.

TAVILY API KEY:
1. Go to https://app.tavily.com/sign-in.
2. Sign up for an account or sign in if you already have one.
3. After logging in, navigate to the "API Key" section on your dashboard/homepage.
4. Copy your API key from that section.


YOUTUBE_API_KEY:
1. Go to Google Cloud Console at https://console.cloud.google.com/.
2. Create or select a project.
3. Enable the YouTube Data API v3 for the project.
4. Go to the "Credentials" section and create an API key.
5. Copy the API key and keep it secure for your app’s use.


API:http://0.0.0.0:5000/api/post
METHOD: POST

PAYLOAD: {"query": "Best laptops brands india","email":"asadsher2324@gmail.com"}

RESPONSE: {"query_id": 5}

API: http://0.0.0.0:5000/api/get/<query_id>  // http://0.0.0.0:5000/api/get/5

METHOD: GET

RESPONSE: {
  "_id": 7,
  "query": "Best smartwatches india",
  "email": "asadsher2324@gmail.com",
  "status": "Searching completed",
  "best_product": {
    "product_name": "Samsung Galaxy Watch8 Classic",
    "justification": "Based on overall ratings, features, and value for money, Samsung Galaxy Watch8 Classic is the best product."
  },
  "products": [
    {
      "title": "Samsung Galaxy Watch8 Classic",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": "34mm",
        "Compatible OS": "Android and iOS",
        "Display Type": "Super AMOLED"
      },
      "score": null,
      "price_range": "₹46,999",
      "brand": "Samsung",
      "category": "Smartwatch"
    },
    {
      "title": "Amazfit GTS 2",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": "42mm",
        "Compatible OS": "Android, iOS",
        "Dial Shape": "Rectangle"
      },
      "score": null,
      "price_range": "₹6,999 - ₹17,999",
      "brand": "Amazfit",
      "category": "Smartwatch"
    },
    {
      "title": "Honor Choice Watch",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": null,
        "Compatible OS": null,
        "Dial Shape": "Rectangle"
      },
      "score": null,
      "price_range": "₹3,899 - ₹8,999",
      "brand": "Honor",
      "category": "Smartwatch"
    },
    {
      "title": "Crossbeats Ignite Atlas",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": null,
        "Compatible OS": "Android, iOS",
        "Dial Shape": "Square"
      },
      "score": null,
      "price_range": "₹2,499 - ₹11,999",
      "brand": "Crossbeats",
      "category": "Smartwatch"
    },
    {
      "title": "TIMEX Fit 2.0",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": "45mm",
        "Compatible OS": null,
        "Dial Shape": "Round"
      },
      "score": null,
      "price_range": "₹3,995 - ₹5,995",
      "brand": "TIMEX",
      "category": "Smartwatch"
    },
    {
      "title": "Portronics Kronos Beta",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": null,
        "Compatible OS": null,
        "Dial Shape": "Round"
      },
      "score": null,
      "price_range": "₹3,999 - ₹5,999",
      "brand": "Portronics",
      "category": "Smartwatch"
    },
    {
      "title": "Noise ColorFit Pulse Grand",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": null,
        "Compatible OS": null,
        "Dial Shape": "Square"
      },
      "score": null,
      "price_range": "₹1,399 - ₹3,999",
      "brand": "Noise",
      "category": "Smartwatch"
    },
    {
      "title": "Noise NoiseFit Evolve 2",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": "42mm",
        "Compatible OS": null,
        "Dial Shape": "Round"
      },
      "score": null,
      "price_range": "₹3,899 - ₹7,999",
      "brand": "Noise",
      "category": "Smartwatch"
    },
    {
      "title": "CMF Watch Pro",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": null,
        "Compatible OS": null,
        "Dial Shape": "Square"
      },
      "score": null,
      "price_range": "₹4,499 - ₹5,999",
      "brand": "CMF",
      "category": "Smartwatch"
    },
    {
      "title": "Redmi Watch 5 Active",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": null,
        "Compatible OS": "Android and iOS",
        "Dial Shape": "Rectangle"
      },
      "score": null,
      "price_range": "₹1,999 - ₹4,999",
      "brand": "Redmi",
      "category": "Smartwatch"
    },
    {
      "title": "Samsung Galaxy Watch 6 Classic",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": "43mm",
        "Compatible OS": null,
        "Dial Shape": "Round"
      },
      "score": null,
      "price_range": "₹18,059 - ₹42,999",
      "brand": "Samsung",
      "category": "Smartwatch"
    },
    {
      "title": "Samsung Galaxy Watch Ultra",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": null,
        "Compatible OS": null,
        "Dial Shape": "Round"
      },
      "score": null,
      "price_range": "₹59,999 - ₹69,999",
      "brand": "Samsung",
      "category": "Smartwatch"
    },
    {
      "title": "Amazfit Active Edge",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": null,
        "Compatible OS": "Android and iOS",
        "Dial Shape": "Round"
      },
      "score": null,
      "price_range": "₹12,999 - ₹19,999",
      "brand": "Amazfit",
      "category": "Smartwatch"
    },
    {
      "title": "Amazfit Active 2",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": null,
        "Compatible OS": "Android and iOS",
        "Dial Shape": "Round"
      },
      "score": null,
      "price_range": "₹9,999 - ₹21,999",
      "brand": "Amazfit",
      "category": "Smartwatch"
    },
    {
      "title": "Gionee StylFit GSW6",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": null,
        "Compatible OS": "Android 4.4 and above, iOS 9.0 and above",
        "Dial Shape": "Rectangle"
      },
      "score": null,
      "price_range": "₹1,766 - ₹6,999",
      "brand": "Gionee",
      "category": "Smartwatch"
    },
    {
      "title": "boAt Storm Infinity",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": "36mm",
        "Compatible OS": null,
        "Dial Shape": "Rectangle"
      },
      "score": null,
      "price_range": "₹1,149 - ₹1,699",
      "brand": "boAt",
      "category": "Smartwatch"
    },
    {
      "title": "boAt Valour Watch 1 GPS",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": "36mm",
        "Compatible OS": null,
        "Dial Shape": "Round"
      },
      "score": null,
      "price_range": "₹5,499 - ₹9,999",
      "brand": "boAt",
      "category": "Smartwatch"
    },
    {
      "title": "Apple Watch Series 6 GPS",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": "40mm",
        "Compatible OS": null,
        "Dial Shape": "Rectangle"
      },
      "score": null,
      "price_range": "₹26,999 - ₹40,900",
      "brand": "Apple",
      "category": "Smartwatch"
    },
    {
      "title": "Fossil Gen 6 (44mm)",
      "url": "https://www.gadgets360.com/wearables/smartwatch-finder",
      "content": "Latest & Best Smartwatches Online 2020",
      "pros": [],
      "cons": [],
      "highlights": {
        "Display Size": "44mm",
        "Compatible OS": null,
        "Dial Shape": "Round"
      },
      "score": null,
      "price_range": "₹11,997 - ₹23,995",
      "brand": "Fossil",
      "category": "Smartwatch"
    }
  ],
  "youtube_link": "https://www.youtube.com/watch?v=APT6FONMqFQ"
}


