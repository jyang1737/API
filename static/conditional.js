//Copyright 2015 Pareto Software, LLC, released under an MIT license: http://opensource.org/licenses/MIT
$( document ).ready(function() {
		//Inputs that determine what fields to show
		var pictype = $('#live_form input:radio[name=pictype]');
		
		//Wrappers for all fields
		var upload = $('#form_upload input[name="upload"]').parent();
		var url = $('#form_URL input[name="URL"]').parent();
		var all= upload.add(url);
		
		pictype.change(function(){
			var value=this.value;						
			all.addClass('hidden'); //hide everything and reveal as needed
			
			if (value == 'upload'){
				url.addClass('hidden');
				$('#live_form input[name="URL"]').val("");
				upload.removeClass('hidden');	
			}
			else if (value == 'URL'){
				upload.addClass('hidden');
				$('#live_form input[name="upload"]').val("");
				url.removeClass('hidden');

			}		
		});	
});
