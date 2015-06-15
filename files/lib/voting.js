var stored_vote = {'error_message': 'none'};

function stored_doVote(){
	//console.log(stored_vote);
	if (stored_vote.error_message == 'Not authenticated.'){
		voteRequest.post({
			'model': 'yardsigns.Sign',
			'object_id': stored_vote.object_id,
			'direction': stored_vote.direction
		});
	}
}


function doVote(data){
	$('ajax-loader_'+data.id).setStyle('display','none');
	var upEffect = new Fx.Morph('voteUp_'+data.id, {duration: 1000, transition: Fx.Transitions.Sine.easeOut});
	var downEffect = new Fx.Morph('voteDown_'+data.id, {duration: 1000, transition: Fx.Transitions.Sine.easeOut});
	var notVote = {
			'background-color': '#cccccc', 
	    	'border-color': '#999999', 
			'color': '#666666'};
	if (data.vote == 1){ 
		upEffect.start({
		    'background-color': '#ccffcc', 
		    'border-color': '#008000', 
			'color': '#008000'
		});
		downEffect.start(notVote);
	}
	if (data.vote == 0){ 
		downEffect.start({
		    'background-color': '#fdcece', 
		    'border-color': '#FF0000', 
			'color': '#FF0000'
		});
		upEffect.start(notVote);
	}

	if (data.score.score < 0){ data.score.score = 0;}

 	if (data.score.score == 1){
		message = "1 person would put this sign in their yard.";
	} else {
		message = data.score.score+" people would put this sign in their yard.";
	}
	$('score_'+data.id).set('text',message);
}

var voteRequest = new Request.JSON({
	url: "vote/", 
	onComplete: function(data){
		if (data.success){
			doVote(data);
		} else if (data.success == false){
			$('ajax-loader_'+data.object_id).setStyle('display','none');
			stored_vote = data;
			//console.log(stored_vote);
			//show the overlay to log in
			TB_show('We require you to register so we can prevent spam and abuse to our system.', '/login/?height=473&width=730&TB_iframe=true','');
		}
	}
});

	
window.addEvent('domready', function(){
	$$('a.vote').each(function(el){
	    el.addEvent('click',function(){
		
			var signId = el.getProperty('signId');
			//console.log($('ajax-loader_'+signId));
			$('ajax-loader_'+signId).setStyle('display','block');
			var direction = '';
			
			if ($(this).hasClass('up')){
				voteRequest.options.url = "/sign/"+signId+"/upvote/";
				direction = "up";
			}
			if ($(this).hasClass('down')){
				voteRequest.options.url = "/sign/"+signId+"/downvote/";
				direction = "down";
			} 
			
			//window.console.log("dir: "+direction);
			voteRequest.post({
				'model': 'yardsigns.Sign',
				'object_id': signId,
				'direction': direction
			});
			return false;
		});
	});
});
