This backend serves as the logic engine for the Style Suggester application, built with Flask to bridge the frontend with the OpenWeatherMap API. 
When a user submits a city name via a POST request to the /suggest endpoint, the backend fetches real-time weather data and applies custom logic 
to categorize the temperature. It then returns a JSON object containing the rounded temperature, a weather description, a tailored outfit suggestion, 
and the specific filename for the corresponding editorial image. By handling the logic here, the application keeps the frontend lightweight and ensures 
that the "Hot," "Mild," or "Cold" style determinations remain consistent and easy to update in one central location.

To maintain high security standards, all sensitive credentials—specifically the OpenWeatherMap API key—are stored as environment variables on the 
Render platform and never exposed in the frontend code or committed to GitHub. This architecture prevents unauthorized API usage and protects the 
developer's account from key theft. For local development, the server can be run by installing flask, flask-cors, and requests, then setting the 
WEATHER_API_KEY in your local environment. The backend also implements a CORS policy to ensure that only the authorized portfolio frontend can 
successfully communicate with the API, providing a secure, professional-grade connection between the two services.

PROMPTS:
- made using gemini
Key Prompts:
1. okay for my frontend HTML i want to put it in my portfolio like when you click the weather app page you are able to do this
2. i got error could not connect to backend
3. how long will it take for the backend to update if i changed the messages
4.  Weather-Based Style Suggestion
​An app that tells you what to wear today.
​The Backend: Calls a Weather API (like OpenWeatherMap) using a secret API key. It processes the temperature and returns a recommendation (e.g., "It's 40°F, wear a heavy coat").
​The Frontend: Asks for the user's city and displays an icon of the recommended clothing. This
