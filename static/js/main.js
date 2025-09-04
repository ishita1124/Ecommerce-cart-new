// Example: confirm before removing item from cart
document.addEventListener("DOMContentLoaded", () => {
    const removeLinks = document.querySelectorAll("a.remove-item");
    removeLinks.forEach(link => {
        link.addEventListener("click", function (e) {
            if (!confirm("Are you sure you want to remove this item from your cart?")) {
                e.preventDefault();
            }
        });
    });
});
