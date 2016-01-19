jQuery(document).ready(function() {
    jQuery('#contexts-dropdown .context-item').on('click', function(e) {
        changeActiveContext.change(jQuery(this));
    });


    jQuery(ajaxFormHandler.forms).on('submit', function(e) {
        e.preventDefault();

        ajaxFormHandler.send(jQuery(this));
    })
});