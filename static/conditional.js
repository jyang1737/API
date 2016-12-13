//Copyright 2015 Pareto Software, LLC, released under an MIT license: http://opensource.org/licenses/MIT
$( document ).ready(function() {
		//Inputs that determine what fields to show
		var pictype = $('#live_form input:radio[name=pictype]');
		
		//Wrappers for all fields
		var upload = $('#live_form input[name="upload"]').parent();
		var url = $('#live_form input[name="URL"]').parent();
		var submit = $('#live_form button[name="submit"]').parent();
		var all=upload.add(url);
		
		pictype.change(function(){
			var value=this.value;						
			all.addClass('hidden'); //hide everything and reveal as needed
			
			if (value == 'upload'){
				upload.removeClass('hidden');	
				$('#live_form input[name="URL"]').val("");
				submit.removeClass('hidden');							
			}
			else if (value == 'URL'){
				url.removeClass('hidden');
				$('#live_form input[name="upload"]').val("");
				submit.removeClass('hidden');	
			}		
		});	
});
