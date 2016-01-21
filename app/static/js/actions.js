jQuery(document).ready(function() {
    jQuery('#contexts-dropdown .context-item').on('click', function(e) {
        changeActiveContext.change(jQuery(this));
    });

    jQuery(ajaxFormHandler.forms).on('submit', function(e) {
        e.preventDefault();

        ajaxFormHandler.send(jQuery(this));
    });

    jQuery(document).on('ajaxSubmitStarted', function(e) {
        e.preventDefault();
        jQuery('#loading-modal').modal('show');
    });

    jQuery(document).on('ajaxSubmitFinished', function(e) {
        e.preventDefault();
        jQuery('#loading-modal').modal('hide');
    });
});

