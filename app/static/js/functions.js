var data_json = '';

var ajaxFormHandler = {
    forms: '#add-context-form, #add-installation-form',
    send: function(form) {
        jQuery.event.trigger({
            type: 'ajaxSubmitStarted'
        });
        jQuery.ajax({
            url: form.attr('action'),
            method: 'POST',
            data: form.serialize(),
            success: function(data) {
                flash.showMessage(data);
                jQuery.event.trigger({
                    type: 'ajaxSubmitFinished'
                });
            }
        });

    }
}

var changeActiveContext = {
    change: function(item) {
        item.addClass('active');
        item.siblings().removeClass('active');
    }
};


var flash = {
    hasErrors: false,
    handleResponse: function(data) {
        if (data.errors) {
            this.hasErrors = true;
            return this.handleError(data.errors);
        }

        return this.handleSuccess(data);
    },
    handleError: function(errors) {
        var message = '';
        for (error_name in errors) {
            message += error_name + ': ' + errors[error_name] + ' <br>';
        }

        return message;
    },
    handleSuccess: function(data) {
        var message = '';
        for (success in data) {
            message += data[success] + ' <br>';
        }

        return message;
    },
    flashMessage: function(message) {
        jQuery('#flashed-messages').addClass((this.hasErrors) ? 'alert-danger' : 'alert-success').show();
        jQuery('#flashed-messages').append('<li>' + message + '</li>');
        jQuery('.modal.form-modal').modal('hide');
        var _this = this;
        setTimeout(function() {
            jQuery('#flashed-messages').hide();
            jQuery('#flashed-messages').html('');
            jQuery('#flashed-messages').removeClass((_this.hasErrors) ? 'alert-danger' : 'alert-success');
            _this.hasErrors = false;
        }, 5000);
    },
    showMessage: function(data) {
        this.flashMessage(this.handleResponse(data));
    }
}



