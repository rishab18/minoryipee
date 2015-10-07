var AjaxFormHelper = (function() {
    function handle400(form, errors) {
        var i = 0;
        if ('non_field_errors' in errors) {
            var non_field_errors = errors['non_field_errors'];
            var non_field_errors_div = $('<div class="non-field-errors"/>');
            for(i = 0; i < non_field_errors.length; i++) {
                non_field_errors_div.append('<small class="error">' + non_field_errors[i] + '</small>');
            }
            form.prepend(non_field_errors_div);
            delete errors['non_field_errors'];
        }
        for (var field_name in errors) {
            var container = form.find('#id_' + field_name + '_container');
            container.addClass('has-error');
            form.find('#id_' + field_name).addClass('invalid');
            var field_errors_div = $('<div class="errors"/>');
            for (i = 0; i < errors[field_name].length; i++) {
                field_errors_div.append('<small class="error">' + errors[field_name][i] + '</small>');
            }
            container.append(field_errors_div);
        }
    }
    function handleErrors(xhr, status, error) {
        var form = $(this);
        if (xhr.status == '400' && xhr.responseJSON && 'errors' in xhr.responseJSON) {
            handle400(form, xhr.responseJSON['errors'])
        }
    }
    function clearErrors() {
        var form = $(this);
        console.log(form);
        form.find('div.non_field_errors').remove();
        form.find('[id^=id_][id$=_container]').removeClass('has-error');
        form.find('div.errors').remove();
        form.find('input').removeClass('invalid');
        form.find('textarea').removeClass('invalid');
        form.find('select').removeClass('invalid');
    }
    function clear() {
        this.reset();
        clearErrors.call(this);
    }
    return {
        handleErrors : handleErrors,
        clearErrors : clearErrors,
        clear : clear,
    }
})();
