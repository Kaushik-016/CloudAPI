document.getElementById("loginForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
      const response = await fetch("https://your-api-url.com/users/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
      });

      const data = await response.json();
      if (response.ok) {
        alert("Login successful!");
        localStorage.setItem("token", data.token); // Store JWT token for authenticated requests
        window.location.href = "home.html"; // Redirect to home or dashboard
      } else {
        alert(`Login failed: ${data.message}`);
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Login failed. Please try again.");
    }
  });
