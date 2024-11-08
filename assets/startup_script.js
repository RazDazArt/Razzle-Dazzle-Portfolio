// Fade out before navigating
document.addEventListener('DOMContentLoaded', (event) => {
document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', function(e) {
        const destination = this.href;
        if (destination) { // Check if href is not empty to avoid JavaScript links
            e.preventDefault(); // Prevent default link behavior
            
            // Fade out the body
            document.body.style.opacity = 0;

            // Wait for the fade out to finish before navigating
            setTimeout(() => {
                window.location.href = destination;
            }, 500); // Adjust the timeout to match your CSS fade duration
        }
    });
});
});

// Fade in when the page is displayed
window.addEventListener('pageshow', (event) => {
document.body.style.opacity = 1;
});

// add in jquery fix
jQuery.htmlPrefilter = function( html ) {
	return html;
};