document.getElementById("signupForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const phone = document.getElementById("phone").value;

    try {
      const response = await fetch("/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"  // Set Content-Type to JSON
        },
        body: JSON.stringify({ name, email, password, phone }) // Send JSON data
      });

      const data = await response.json();
      if (response.ok) {
        alert("Signup successful!");
        window.location.href = "login.html"; // Redirect to login page
      } else {
        alert(`Signup failed: ${data.message}`);
      }
    } catch (error) {
      console.error("Error:", error);
      alert("Signup failed. Please try again.");
    }
});
