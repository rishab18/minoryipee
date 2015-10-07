var searchProduct = (function() {
	function updateResults(items) {
        if (items.length === 0 ) {
            $('.collection-header').html('No Results!');
        } else {
            $('.collection-header').html(items.length + ' items found');
        }
        $('.collection-item').remove();
        for (var i = 0; i < items.length; i++) {
            var el = $('<li class="collection-item"/>');
            el.html(items[i].name);
            $('.collection').append(el);
        }
    }
	function getProducts {
		$.ajax( {
			url: '/account/search_product'
			data: { name : $('#id_name').val() },
			type: 'GET',
			success: function(data, status, xhr) {
            	updateResults(data['items']);
            }
		} );
	}
	function init() {
		$('#id_name').on('input',getProducts);
	}
	return {
		'init' : init,
	};
})();
$(document).ready(searchProduct.init);



