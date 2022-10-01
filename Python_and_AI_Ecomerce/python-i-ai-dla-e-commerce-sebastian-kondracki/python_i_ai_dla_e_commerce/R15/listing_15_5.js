function() {
    try {
        return
        document.cookie.match(/_ga=(.+?);/)[1].split('.').slice(-2).join(".");
    }
    catch (e) {
        console.log("Error fetching clientId");
        return "n/a";
    }
}