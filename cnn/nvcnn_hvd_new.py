


<!DOCTYPE html>
<html lang="en-US" >

<head>

	
	<script>
window.ts_endpoint_url = "https:\/\/slack.com\/beacon\/timing";

(function(e) {
	var n=Date.now?Date.now():+new Date,r=e.performance||{},t=[],a={},i=function(e,n){for(var r=0,a=t.length,i=[];a>r;r++)t[r][e]==n&&i.push(t[r]);return i},o=function(e,n){for(var r,a=t.length;a--;)r=t[a],r.entryType!=e||void 0!==n&&r.name!=n||t.splice(a,1)};r.now||(r.now=r.webkitNow||r.mozNow||r.msNow||function(){return(Date.now?Date.now():+new Date)-n}),r.mark||(r.mark=r.webkitMark||function(e){var n={name:e,entryType:"mark",startTime:r.now(),duration:0};t.push(n),a[e]=n}),r.measure||(r.measure=r.webkitMeasure||function(e,n,r){n=a[n].startTime,r=a[r].startTime,t.push({name:e,entryType:"measure",startTime:n,duration:r-n})}),r.getEntriesByType||(r.getEntriesByType=r.webkitGetEntriesByType||function(e){return i("entryType",e)}),r.getEntriesByName||(r.getEntriesByName=r.webkitGetEntriesByName||function(e){return i("name",e)}),r.clearMarks||(r.clearMarks=r.webkitClearMarks||function(e){o("mark",e)}),r.clearMeasures||(r.clearMeasures=r.webkitClearMeasures||function(e){o("measure",e)}),e.performance=r,"function"==typeof define&&(define.amd||define.ajs)&&define("performance",[],function(){return r}) // eslint-disable-line
})(window);

</script>
<script>


;(function() {



window.TSMark = function(mark_label) {
	if (!window.performance || !window.performance.mark) return;
	performance.mark(mark_label);
};
window.TSMark('start_load');


window.TSMeasureAndBeacon = function(measure_label, start_mark_label) {
	if (start_mark_label === 'start_nav' && window.performance && window.performance.timing) {
		window.TSBeacon(measure_label, (new Date()).getTime() - performance.timing.navigationStart);
		return;
	}
	if (!window.performance || !window.performance.mark || !window.performance.measure) return;
	performance.mark(start_mark_label + '_end');
	try {
		performance.measure(measure_label, start_mark_label, start_mark_label + '_end');
		window.TSBeacon(measure_label, performance.getEntriesByName(measure_label)[0].duration);
	} catch (e) {
		
	}
};


if ('sendBeacon' in navigator) {
	window.TSBeacon = function(label, value) {
		var endpoint_url = window.ts_endpoint_url || 'https://slack.com/beacon/timing';
		navigator.sendBeacon(endpoint_url + '?data=' + encodeURIComponent(label + ':' + value), '');
	};
} else {
	window.TSBeacon = function(label, value) {
		var endpoint_url = window.ts_endpoint_url || 'https://slack.com/beacon/timing';
		(new Image()).src = endpoint_url + '?data=' + encodeURIComponent(label + ':' + value);
	};
}
})();
</script>
 

<script>
window.TSMark('step_load');
</script>	<noscript><meta http-equiv="refresh" content="0; URL=/?redir=%2Ffiles%2FU9HP5NQ68%2FF9V0TRG8H%2Fnvcnn_hvd.py&amp;nojsmode=1" /></noscript>
<script type="text/javascript">
if(self!==top)window.document.write("\u003Cstyle>body * {display:none !important;}\u003C\/style>\u003Ca href=\"#\" onclick="+
"\"top.location.href=window.location.href\" style=\"display:block !important;padding:10px\">Go to Slack.com\u003C\/a>");

(function() {
	var timer;
	if (self !== top) {
		timer = window.setInterval(function() {
			if (window.$) {
				try {
					$('#page').remove();
					$('#client-ui').remove();
					window.TS = null;
					window.clearInterval(timer);
				} catch(e) {}
			}
		}, 200);
	}
}());

</script>

<script>

(function() {


	window.callSlackAPIUnauthed = function(method, args, callback) {
		var timestamp = Date.now() / 1000;  
		var version = (window.TS && TS.boot_data && TS.boot_data.version_uid) ? TS.boot_data.version_uid.substring(0, 8) : 'noversion';
		var url = '/api/' + method + '?_x_id=' + version + '-' + timestamp;

		var req = new XMLHttpRequest();

		req.onreadystatechange = function() {
			if (req.readyState == 4) {
				req.onreadystatechange = null;
				var obj;

				if (req.status == 200 || req.status == 429) {
					try {
						obj = JSON.parse(req.responseText);
					} catch (err) {
						TS.warn(8675309, 'unable to do anything with api rsp');
					}
				}

				obj = obj || {
					ok: false,
				};

				callback(obj.ok, obj, args);
			}
		};

		var async = true;
		req.open('POST', url, async);

		var form_data = new FormData();
		var has_data = false;
		Object.keys(args).forEach(function(k) {
			if (k[0] === '_') return;
			form_data.append(k, args[k]);
			has_data = true;
		});

		if (has_data) {
			req.send(form_data);
		} else {
			req.send();
		}
	};
})();
</script>

	<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/webpack.manifest.d9a2676e14e30bd41692.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>

			
	
		<script>
			if (window.location.host == 'slack.com' && window.location.search.indexOf('story') < 0) {
				document.cookie = '__cvo_skip_doc=' + escape(document.URL) + '|' + escape(document.referrer) + ';path=/';
			}
		</script>
	

		<script type="text/javascript">
		
		try {
			if(window.location.hash && !window.location.hash.match(/^(#?[a-zA-Z0-9_]*)$/)) {
				window.location.hash = '';
			}
		} catch(e) {}
		
	</script>

	<script type="text/javascript">
				
			window.optimizely = [];
			window.dataLayer = [];
			window.ga = false;
		
	
				(function(e,c,b,f,d,g,a){e.SlackBeaconObject=d;
		e[d]=e[d]||function(){(e[d].q=e[d].q||[]).push([1*new Date(),arguments])};
		e[d].l=1*new Date();g=c.createElement(b);a=c.getElementsByTagName(b)[0];
		g.async=1;g.src=f;a.parentNode.insertBefore(g,a)
		})(window,document,"script","https://a.slack-edge.com/bv1-1/slack_beacon.5dbbc3dd9f37d8bc2f4e.min.js","sb");
		sb('set', 'token', '3307f436963e02d4f9eb85ce5159744c');

				sb('track', 'pageview');

		
		function track(a) {
			if(window.ga) ga('send','event','web', a);
			if(window.sb) sb('track', a);
		}
		

	</script>

	

	<meta name="referrer" content="no-referrer">
		<meta name="superfish" content="nofish">

	<script type="text/javascript">



var TS_last_log_date = null;
var TSMakeLogDate = function() {
	var date = new Date();

	var y = date.getFullYear();
	var mo = date.getMonth()+1;
	var d = date.getDate();

	var time = {
	  h: date.getHours(),
	  mi: date.getMinutes(),
	  s: date.getSeconds(),
	  ms: date.getMilliseconds()
	};

	Object.keys(time).map(function(moment, index) {
		if (moment == 'ms') {
			if (time[moment] < 10) {
				time[moment] = time[moment]+'00';
			} else if (time[moment] < 100) {
				time[moment] = time[moment]+'0';
			}
		} else if (time[moment] < 10) {
			time[moment] = '0' + time[moment];
		}
	});

	var str = y + '/' + mo + '/' + d + ' ' + time.h + ':' + time.mi + ':' + time.s + '.' + time.ms;
	if (TS_last_log_date) {
		var diff = date-TS_last_log_date;
		//str+= ' ('+diff+'ms)';
	}
	TS_last_log_date = date;
	return str+' ';
}

var parseDeepLinkRequest = function(code) {
	var m = code.match(/"id":"([CDG][A-Z0-9]{8})"/);
	var id = m ? m[1] : null;

	m = code.match(/"team":"(T[A-Z0-9]{8})"/);
	var team = m ? m[1] : null;

	m = code.match(/"message":"([0-9]+\.[0-9]+)"/);
	var message = m ? m[1] : null;

	return { id: id, team: team, message: message };
}

if ('rendererEvalAsync' in window) {
	var origRendererEvalAsync = window.rendererEvalAsync;
	window.rendererEvalAsync = function(blob) {
		try {
			var data = JSON.parse(decodeURIComponent(atob(blob)));
			if (data.code.match(/handleDeepLink/)) {
				var request = parseDeepLinkRequest(data.code);
				if (!request.id || !request.team || !request.message) return;

				request.cmd = 'channel';
				TSSSB.handleDeepLinkWithArgs(JSON.stringify(request));
				return;
			} else {
				origRendererEvalAsync(blob);
			}
		} catch (e) {
		}
	}
}
</script>



<script type="text/javascript">

	var TSSSB = {
		call: function() {
			return false;
		}
	};

</script>
<script>TSSSB.env = (function() {


	var v = {
		win_ssb_version: null,
		win_ssb_version_minor: null,
		mac_ssb_version: null,
		mac_ssb_version_minor: null,
		mac_ssb_build: null,
		lin_ssb_version: null,
		lin_ssb_version_minor: null,
		desktop_app_version: null,
	};

	var is_win = (navigator.appVersion.indexOf('Windows') !== -1);
	var is_lin = (navigator.appVersion.indexOf('Linux') !== -1);
	var is_mac = !!(navigator.userAgent.match(/(OS X)/g));

	if (navigator.userAgent.match(/(Slack_SSB)/g) || navigator.userAgent.match(/(Slack_WINSSB)/g)) {
		
		var parts = navigator.userAgent.split('/');
		var version_str = parts[parts.length - 1];
		var version_float = parseFloat(version_str);
		var version_parts = version_str.split('.');
		var version_minor = (version_parts.length == 3) ? parseInt(version_parts[2], 10) : 0;

		if (navigator.userAgent.match(/(AtomShell)/g)) {
			
			if (is_lin) {
				v.lin_ssb_version = version_float;
				v.lin_ssb_version_minor = version_minor;
			} else if (is_win) {
				v.win_ssb_version = version_float;
				v.win_ssb_version_minor = version_minor;
			} else if (is_mac) {
				v.mac_ssb_version = version_float;
				v.mac_ssb_version_minor = version_minor;
			}

			if (version_parts.length >= 3) {
				v.desktop_app_version = {
					major: parseInt(version_parts[0], 10),
					minor: parseInt(version_parts[1], 10),
					patch: parseInt(version_parts[2], 10),
				};
			}
		}
	}

	return v;
})();
</script>


	<script type="text/javascript">
		
		window.addEventListener('load', function() {
			var was_TS = window.TS;
			delete window.TS;
			if (was_TS) window.TS = was_TS;
		});
	</script>
	        <title>Slack</title>
    <meta name="author" content="Slack">
        
    <meta name="robots" content="noindex,nofollow">

	
		
	
	
		
					
	
						
	
	

																
	
	
	
	
	
	
		<!-- output_css "sk_adapter" -->
    <link href="https://a.slack-edge.com/7057c/style/rollup-slack_kit_legacy_adapters.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)">

			<!-- output_css "core" -->
    <link href="https://a.slack-edge.com/005d9/style/rollup-plastic.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)">

		<!-- output_css "before_file_pages" -->

	<!-- output_css "file_pages" -->

	
			<!-- output_css "slack_kit_helpers" -->
    <link href="https://a.slack-edge.com/58329/style/rollup-slack_kit_helpers.css" rel="stylesheet" type="text/css" id="slack_kit_helpers_stylesheet"  crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)">

	<!-- output_css "regular" -->
    <link href="https://a.slack-edge.com/e433/style/signin.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)">
    <link href="https://a.slack-edge.com/698de/style/index.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)">
    <link href="https://a.slack-edge.com/5e83b/style/libs/lato-2-compressed.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)">
    <link href="https://a.slack-edge.com/c4512/style/sticky_nav.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)">
    <link href="https://a.slack-edge.com/176a/style/footer.css" rel="stylesheet" type="text/css" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)">

	

	
	
		<meta name="robots" content="noindex, nofollow" />
	

	
<link id="favicon" rel="shortcut icon" href="https://a.slack-edge.com/436da/marketing/img/meta/favicon-32.png" sizes="16x16 32x32 48x48" type="image/png" />

<link rel="icon" href="https://a.slack-edge.com/436da/marketing/img/meta/app-256.png" sizes="256x256" type="image/png" />

<link rel="apple-touch-icon-precomposed" sizes="152x152" href="https://a.slack-edge.com/436da/marketing/img/meta/ios-152.png" />
<link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://a.slack-edge.com/436da/marketing/img/meta/ios-144.png" />
<link rel="apple-touch-icon-precomposed" sizes="120x120" href="https://a.slack-edge.com/436da/marketing/img/meta/ios-120.png" />
<link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://a.slack-edge.com/436da/marketing/img/meta/ios-114.png" />
<link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://a.slack-edge.com/436da/marketing/img/meta/ios-72.png" />
<link rel="apple-touch-icon-precomposed" href="https://a.slack-edge.com/436da/marketing/img/meta/ios-57.png" />

<meta name="msapplication-TileColor" content="#FFFFFF" />
<meta name="msapplication-TileImage" content="https://a.slack-edge.com/436da/marketing/img/meta/app-144.png" />
	
</head>

<body class="	index			deprecated">

		  			<script>
		
			var w = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);
			if (w > 1440) document.querySelector('body').classList.add('widescreen');
		
		</script>
	
  	
	
	

	
					

	



	<nav class="top persistent">
	
		
		<a href="https://slack.com/" class="logo" data-qa="logo" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=logo" aria-label="Slack homepage"></a>
	
		
							
					<ul>
				<li><a  href="https://slack.com/is" data-qa="product" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_product">Product</a></li>
				<li><a  href="https://slack.com/pricing?ui_step=55&ui_element=5" data-qa="pricing" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_pricing">Pricing</a></li>				<li><a  href="https://get.slack.help/hc/en-us" data-qa="support" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_support">Support</a></li>

								<li class= "mobile_btn download_slack"><a  href="/get" data-qa="download_slack" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_download">Download Slack</a></li>									<li><a data-gtm-click="SignUp,optout_nav_create_team" href="https://slack.com/create" class="" data-qa="create_team" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_create_team">Create a new workspace</a></li>
					<li><a  href="https://slack.com/get-started" data-gtm-click="optout_nav_find_team" data-qa="find_team" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_find_team">Find your workspace</a></li>

					<li class="sign_in hide_on_mobile"><a data-gtm-click="optout_nav_signin" href="https://slack.com/signin" class="btn_sticky btn_filled" data-qa="sign_in" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_sign_in">Sign in</a></li>
								<li class="mobile_btn mobile_menu_btn">
					<a href="#" class="btn_sticky" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_mobile_menu_btn">Menu</a>
				</li>
			</ul>

			
			</nav>



<nav class="mobile_menu loading menu_scroll" aria-hidden="true">
	<div class="mobile_menu_wrapper">
	<div class="mobile_menu_header">
			<a href="https://slack.com/" class="logo" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_logo"></a>
			<a href="#" class="close" aria-label="close" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_menu_close"><ts-icon class="ts_icon ts_icon_times"></ts-icon></a>
	</div>
					<ul>
				<li><a  href="https://slack.com/is" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_product">Product</a></li>
				<li><a  href="https://slack.com/pricing?ui_step=55&ui_element=5" class="mobile_nav_pricing" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_pricing">Pricing</a></li>				<li><a  href="https://get.slack.help/hc/en-us" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_support">Support</a></li>
				<li><a  href="/get" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_download">Download <span class="optional_desktop_nav_message">the Slack app</span></a></li>
			</ul>

			<ul class="mobile_menu_footer">
				
				<li><a href="https://slack.com/signin" data-gtm-click="optout_nav_signin" target="_blank" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_sign_in"><ts-icon class="ts_icon small float_none team_icon ts_icon_plus default signup_icon"></ts-icon> <span class="switcher_label">Sign in</span></a></li>

				<li><a data-gtm-click="SignUp,optout_nav_create_team" href="https://slack.com/create" class="" target="_blank" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=nav_create_team"><ts-icon class="ts_icon small float_none team_icon ts_icon_slack_pillow default signup_icon"></ts-icon> <span class="switcher_label">Create a new workspace</span></a></li>			</ul>
			</div>
</nav>

	
	<div id="page" >

		<div id="page_contents" data-qa="page_contents" class="">

<div class="span_4_of_6 col float_none margin_auto no_right_padding">
	
		<p class="alert alert_info"><i class="ts_icon ts_icon_info_circle"></i> You need to sign in to see this page.</p>

	
<p id="error_ratelimit" class="alert alert_warning" style="display: none;">
	<i class="ts_icon ts_icon_warning"></i>
	
	<strong>Too many login failures!</strong><br class="hide_on_mobile" />
	Apologies! There were too many SMS message requests in a short period, so you’ll have to wait a moment to try again.
	</p>
<p id="error_unknown" class="alert alert_error" style="display: none;">
	<i class="ts_icon ts_icon_warning"></i> Hmmm... something went wrong. Please try again.</p></div>

	
<div class="real_content card align_center span_4_of_6 col float_none margin_auto large_bottom_margin right_padding large_bottom_padding">
	<h1 id="signin_header" class="tiny_bottom_margin"> 
	Sign in to <span class="break_word">TF-AWS-NV</span>
	</h1>

	<p class="medium_bottom_margin">tf-aws-nv.slack.com</p>

	
	<div class="col span_4_of_6 float_none margin_auto signin_card">
		<form id="signin_form" action="/" method="post" accept-encoding="UTF-8">
			<input type="hidden" name="signin" value="1">
			<input type="hidden" name="redir" value="/files/U9HP5NQ68/F9V0TRG8H/nvcnn_hvd.py">
						<input type="hidden" name="crumb" value="s-1521916250-0aad5f2323959a9184ce3d08450d4c6194a0315da515f055240a88fc6940ae8c-☃" />

			<p class="browser_password align_left">Enter your <strong>email address</strong> and <strong>password</strong>.</p>
			<p class="ssb_password hidden">What is your <strong>password</strong>?</p>

			<p class=" no_bottom_margin">
				<input type="email" id="email" name="email" size="40" value="" placeholder="you@example.com">
			</p>

			<p class=" small_bottom_margin">
				<input type="password" id="password" name="password" size="40" placeholder="password" >
			</p>

			
						

			<p><button id="signin_btn" type="submit" class="btn btn_large full_width ladda-button" data-style="expand-right"><span class="ladda-label">Sign in</span></button></p>

			<div class="align_left">
				<label class="checkbox normal inline_block small_right_margin"><input type="checkbox" name="remember" checked> Remember me</label>
			</div>
	
			<div class="align_left small_top_margin">
				<a id="forgot-pw" href="/forgot">Forgot password?</a>
									· <a href="https://slack.com/get-started">Forgot which email you used?</a>
							</div>

		</form>
		<div id="magic_login_cta" class="float_none margin_auto hidden">

   		<div class="or no_wrap small_top_padding medium_bottom_margin align_center">or</div>

			 <p class="large_bottom_margin"><strong>Long password? Hard to type?</strong><br /> We can email you a magic link so you can sign in without having to type your password.</p>

			<form id="magic_login" action="/" method="post" accept-encoding="UTF-8" class="align_center float_none margin_auto medium_bottom_margin">
				<input type="hidden" name="crumb" value="s-1521916250-0aad5f2323959a9184ce3d08450d4c6194a0315da515f055240a88fc6940ae8c-☃" />
				<input type="hidden" name="email">
				<input type="hidden" name="signin_request_magiclogin" value="1">
				<button class="btn btn_large btn_outline full_width"><ts-icon class="ts_icon_magic"></ts-icon>Email Me A Link</button>
			</form>	

		</div>


	</div>

	<p class="small clear_both taller_line_height">
			</p>
</div>
	
<div class="real_content align_center">
			<p>
			<span class="bold">Don't have an account on this workspace yet?</span>
			<span class="clear_both block">Contact the workspace administrator for an invitation</span>
		</p>
	
	
			<p>
			Trying to create a workspace?			
	
	<a data-gtm-click="SignUp" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=inc_download_app_or_sign_in_cta_sign_up_link" href="/create" class="bold">Create a new workspace</a>
			</p>
	</div>

					
	</div>
	<div id="overlay"></div>
</div>


	


<footer  data-qa="footer">
	<section class="links">
		<div class="grid">
			<div class="col span_1_of_4 nav_col">
				<ul>
					<li class="cat_1">Using Slack</li>
					<li><a href="/is" data-qa="product_footer" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_product">Product</a></li>
					<li><a href="/enterprise" data-qa="enterprise_footer" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_enterprise">Enterprise</a></li>
					<li><a href="/pricing?ui_step=28&ui_element=5" data-qa="pricing_footer" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_pricing">Pricing</a></li>
					<li><a href="https://get.slack.help/hc/en-us" data-qa="support_footer" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_support">Support</a></li>
					<li><a href="/guides" data-qa="getting_started" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_getting_started">Slack Guides</a></li>
					<li><a href="/apps" data-qa="app_directory" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_app_directory">App Directory</a></li>
					<li><a href="https://api.slack.com/" data-qa="api" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_api">API</a></li>
				</ul>
			</div>
			<div class="col span_1_of_4 nav_col">
				<ul>
					<li class="cat_2">Slack <ts-icon class="ts_icon_heart"></ts-icon></li>
					<li><a href="/jobs" data-qa="jobs" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_jobs">Jobs</a></li>
					<li><a href="/customers" data-qa="customers" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_customers">Customers</a></li>
					<li><a href="/developers" data-qa="developers" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_developers">Developers</a></li>
					<li><a href="/events" data-qa="events" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_events">Events</a></li>
					<li><a href="https://slackhq.com/" data-qa="blog_footer" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_blog">Blog</a></li>
					<li><a href="/podcast" data-qa="podcast" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_podcast">Podcast</a></li>
					<li><a href="https://slack.shop/" data-qa="slack_shop" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_slack_shop">Slack Shop</a></li>
				</ul>
			</div>
			<div class="col span_1_of_4 nav_col">
				<ul>
					<li class="cat_3">Legal</li>
					<li><a href="/privacy-policy" data-qa="privacy" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_privacy">Privacy</a></li>
					<li><a href="/security" data-qa="security" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_security">Security</a></li>
					<li><a href="/terms-of-service" data-qa="tos" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_tos">Terms of Service</a></li>
					<li><a href="/policies" data-qa="policies" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_policies">Policies</a></li>
				</ul>
			</div>
			<div class="col span_1_of_4 nav_col">
				<ul>
					<li class="cat_4">Handy Links</li>
					<li><a href="/downloads" data-qa="downloads" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_downloads">Download desktop app</a></li>
					<li><a href="/downloads" data-qa="downloads_mobile" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_downloads_mobile">Download mobile app</a></li>
					<li><a href="/brand-guidelines" data-qa="brand_guidelines" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_brand_guidelines">Brand Guidelines</a></li>
					<li><a href="https://slackatwork.com" data-qa="slack_at_work" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_slack_at_work">Slack at Work</a></li>
					<li><a href="https://status.slack.com/" data-qa="status" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_status">Status</a></li>
				</ul>
			</div>
		</div>
	</section>

	<div class="footnote">
		<section>
			<a href="https://slack.com" aria-label="Slack homepage" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_slack_icon"><ts-icon class="ts_icon_slack_pillow" aria-hidden="true"></ts-icon></a>
			<ul>
				<li>
					<a href="/help/contact" data-qa="contact_us" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_contact_us">Contact Us</a>
				</li>
				<li>
					<a href="https://twitter.com/SlackHQ" data-qa="slack_twitter" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_slack_twitter" aria-label="Slack on Twitter"><ts-icon class="ts_icon_twitter" aria-hidden="true"></ts-icon></a>
				</li>
				<li class="yt">
					<a href="https://www.youtube.com/channel/UCY3YECgeBcLCzIrFLP4gblw" data-qa="slack_youtube" data-clog-event="WEBSITE_CLICK" data-clog-params="click_target=footer_slack_youtube" aria-label="Slack on YouTube"><ts-icon class="ts_icon_youtube" aria-hidden="true"></ts-icon></a>
				</li>
			</ul>
		</section>
	</div>
</footer>





<script type="text/javascript">

	/**
	 * A placeholder function that the build script uses to
	 * replace file paths with their CDN versions.
	 *
	 * @param {String} file_path - File path
	 * @returns {String}
	 */
	function vvv(file_path) {

		var vvv_warning = 'You cannot use vvv on dynamic values. Please make sure you only pass in static file paths.';
		if (TS && TS.warn) {
			TS.warn(vvv_warning);
		} else {
			console.warn(vvv_warning);
		}

		return file_path;
	}

	var cdn_url = "https:\/\/a.slack-edge.com";
	var vvv_abs_url = "https:\/\/slack.com\/";
	var inc_js_setup_data = {
			emoji_sheets: {
			apple: 'https://a.slack-edge.com/c00d19/img/emoji_2017_12_06/sheet_apple_64_indexed_256.png',
			google: 'https://a.slack-edge.com/c00d19/img/emoji_2017_12_06/sheet_google_64_indexed_256.png',
		},
		emoji5: true,
		};
</script>
	<script type="text/javascript">
<!--
	// common boot_data
	var boot_data = {
		start_ms: Date.now(),
		app: "web",
		user_id: '',
		team_id: 'T00',
		visitor_uid: "1c68s3w3u87400ccogskc4o4c",
		no_login: true,
		version_ts: "1521903667",
		version_uid: "994744788f157f504d4123016987a792d9ade09c",
		cache_version: "v16-giraffe",
		cache_ts_version: "v2-bunny",
		redir_domain: "slack-redir.net",
		signin_url: 'https://slack.com/signin',
		abs_root_url: "https:\/\/slack.com\/",
		api_url: '/api/',
		team_url: "",
		image_proxy_url: "https:\/\/slack-imgs.com\/",
		beacon_timing_url: "https:\/\/slack.com\/beacon\/timing",
		beacon_error_url: "https:\/\/slack.com\/beacon\/error",
		clog_url: "clog\/track\/",
		api_token: "",
		ls_disabled: false,
		hc_tracking_qs: "",

		vvv_paths: {
			
		lz_string: "https:\/\/a.slack-edge.com\/bv1-1\/lz-string-1.4.4.worker.8de1b00d670ff3dc706a0.js",
		codemirror: "https:\/\/a.slack-edge.com\/bv1-1\/codemirror.min.44a2b0ae2d7a5cac8a95.min.js",
	codemirror_addon_simple: "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_simple.9c76f7896754967b9eda.min.js",
	codemirror_load: "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_load.ca4f26b018edcede90ce.min.js",

	// Silly long list of every possible file that Codemirror might load
	codemirror_files: {
		'apl': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_apl.28ce658730a18a115532.min.js",
		'asciiarmor': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_asciiarmor.b6cae5185b1e92ac1917.min.js",
		'asn.1': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_asn.1.1992736a46ff4b01f93f.min.js",
		'asterisk': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_asterisk.8dc14a25826407ab1fa3.min.js",
		'brainfuck': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_brainfuck.d29773c7ac178228d4c1.min.js",
		'clike': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_clike.cccd21c94a2b7ab7ce3d.min.js",
		'clojure': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_clojure.4a91a0c50a64467f2ff5.min.js",
		'cmake': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_cmake.a873ff1604fb8e89955f.min.js",
		'cobol': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_cobol.2b7098fad4936f18f361.min.js",
		'coffeescript': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_coffeescript.68a8fdd315d0dcf8c27a.min.js",
		'commonlisp': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_commonlisp.879f5b578b25a058fc4d.min.js",
		'css': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_css.035ca224464953138c30.min.js",
		'crystal': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_crystal.79beb330be1a294e43c4.min.js",
		'cypher': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_cypher.525ea24cf7710ac2825a.min.js",
		'd': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_d.7328ff9ab8c98103deb7.min.js",
		'dart': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_dart.f7e22fcf397d31e7af93.min.js",
		'diff': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_diff.c3b6cf00600144071d6d.min.js",
		'django': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_django.cde302c62fe6365529f2.min.js",
		'dockerfile': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_dockerfile.ed0e37e03b2023e1b69b.min.js",
		'dtd': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_dtd.df3795754645134d5f80.min.js",
		'dylan': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_dylan.fed72f1d0e846fd6d213.min.js",
		'ebnf': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_ebnf.6af113fdedf587f96c64.min.js",
		'ecl': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_ecl.12b9206b24a5433649ab.min.js",
		'eiffel': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_eiffel.896ceb473406cc01ee59.min.js",
		'elm': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_elm.637ce7bda68e33c4b55a.min.js",
		'erlang': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_erlang.ea42edc0caacbb7b9429.min.js",
		'factor': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_factor.937f3b4ba675a2abe9c7.min.js",
		'forth': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_forth.89f6ec54d5548d4cf25b.min.js",
		'fortran': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_fortran.e312d7972b690a22beab.min.js",
		'gas': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_gas.abc6e9d7c3a0b887ff69.min.js",
		'gfm': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_gfm.8fc0c8e3735d10a858c6.min.js",
		'gherkin': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_gherkin.9e0cfa25c1965e495419.min.js",
		'go': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_go.5ed96d85ab19d7795ba7.min.js",
		'groovy': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_groovy.c496c31bd5cca0986ead.min.js",
		'haml': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_haml.f25c65cf09f1ec3a29c7.min.js",
		'handlebars': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_handlebars.80eb7b9e2e0fb6dee382.min.js",
		'haskell': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_haskell.e7b2cc288c6bd281ff32.min.js",
		'haxe': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_haxe.3efebdfa3dc7fb7cc4db.min.js",
		'htmlembedded': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_htmlembedded.1a2496c621f9a470c340.min.js",
		'htmlmixed': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_htmlmixed.caa675603dc4fdb90c31.min.js",
		'http': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_http.c1c249d14bf18521fee1.min.js",
		'idl': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_idl.715601d44fbe133c065b.min.js",
		'jade': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_jade.0eff9474d977d43feced.min.js",
		'javascript': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_javascript.bc1b5c6a6515b3064108.min.js",
		'jinja2': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_jinja2.5de8bc52face9b2769f2.min.js",
		'julia': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_julia.32d8748fecc17e6305bf.min.js",
		'livescript': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_livescript.f6dbad1e8d8168b319f4.min.js",
		'lua': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_lua.32780d85e5cbbb59b8eb.min.js",
		'markdown': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_markdown.a7f65f93ece1f31b9e60.min.js",
		'mathematica': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_mathematica.48dd3694f2f71a75544c.min.js",
		'mirc': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_mirc.0f3984162d72c3a0a5ca.min.js",
		'mllike': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_mllike.e4e86126535bd4f7a575.min.js",
		'modelica': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_modelica.d4fd8938619f5c8dc361.min.js",
		'mscgen': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_mscgen.f9d5ab8e95b697c39880.min.js",
		'mumps': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_mumps.b361377133b59678d3d5.min.js",
		'nginx': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_nginx.524bfc39589c37f74bfd.min.js",
		'nsis': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_nsis.b25852c3418f984ae03d.min.js",
		'ntriples': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_ntriples.4e0443a64025c35438a6.min.js",
		'octave': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_octave.3a0c99a5e07bbd9a6d67.min.js",
		'oz': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_oz.e9939d375a47087f59aa.min.js",
		'pascal': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_pascal.f1162aeab4a781363ccd.min.js",
		'pegjs': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_pegjs.7af50308b76ba3251b02.min.js",
		'perl': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_perl.5a7940afe30ba510820a.min.js",
		'php': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_php.64b619fb529d1cd9b781.min.js",
		'pig': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_pig.a30ec6f3ffff33476ac4.min.js",
		'powershell': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_powershell.0ccd1b6a33eb2209c15b.min.js",
		'properties': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_properties.5c0c1436978bf2a7af00.min.js",
		'puppet': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_puppet.53ac0d4fadd68369610e.min.js",
		'python': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_python.dd3e2e25db7e7fb868d6.min.js",
		'q': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_q.4af8c1d9b07ea218977f.min.js",
		'r': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_r.783001720b360a8177a8.min.js",
		'rpm': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_rpm.79678546fb25c75e3208.min.js",
		'rst': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_rst.0fa19c56ae79c0b70c27.min.js",
		'ruby': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_ruby.efce7fd348530776314b.min.js",
		'rust': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_rust.b148ea62a65dfe9f36c0.min.js",
		'sass': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_sass.4e58ddf440975d3864f6.min.js",
		'scheme': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_scheme.52a48304089db7f7708e.min.js",
		'shell': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_shell.8dd47832ce011f080fb8.min.js",
		'sieve': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_sieve.dc92cd9b919e5efb3c05.min.js",
		'slim': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_slim.ba0d300bced932d16420.min.js",
		'smalltalk': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_smalltalk.6dd6e1d419b04500b385.min.js",
		'smarty': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_smarty.428329a9fdb0d8be2a5f.min.js",
		'solr': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_solr.02f1fe78feb4a670b6cc.min.js",
		'soy': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_soy.8145a09e761fee4b0667.min.js",
		'sparql': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_sparql.cf7a2190284c6ca0c11d.min.js",
		'spreadsheet': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_spreadsheet.eeeb35132617f7fa05e6.min.js",
		'sql': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_sql.78a665f0a117e62e46f2.min.js",
		'stex': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_stex.777bff71a93e84be5096.min.js",
		'stylus': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_stylus.6ae0e46fb8c0750c644c.min.js",
		'swift': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_swift.2254c736e8a7f4f51e92.min.js",
		'tcl': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_tcl.13833d90818d7aa20cc6.min.js",
		'textile': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_textile.aa7de5d427d0474f6e14.min.js",
		'tiddlywiki': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_tiddlywiki.efa88c874dc2653bb47e.min.js",
		'tiki': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_tiki.6a8e59872a533ec09dae.min.js",
		'toml': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_toml.4e099e2ec0d834eb7c04.min.js",
		'tornado': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_tornado.feede7e509e683f0998f.min.js",
		'troff': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_troff.d31a17f22f8c679cf3e5.min.js",
		'ttcn': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_ttcn.1bf6637cf05b45897ccd.min.js",
		'ttcn:cfg': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_ttcn-cfg.273e541df1ddc66215ca.min.js",
		'turtle': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_turtle.4cf803c3d74096bfb82a.min.js",
		'twig': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_twig.628d79da0aea153a66fe.min.js",
		'vb': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_vb.828b80361395c4e24aaf.min.js",
		'vbscript': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_vbscript.e19473b2883a8f5e9270.min.js",
		'velocity': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_velocity.09039c2d8f038c5046b2.min.js",
		'verilog': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_verilog.f12abef9991c95696bf5.min.js",
		'vhdl': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_vhdl.6438b130790bb71537f5.min.js",
		'vue': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_vue.b7dca682b49e1cb360cf.min.js",
		'xml': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_xml.c067158d12d43b9b96f7.min.js",
		'xquery': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_xquery.340466967c2bdf65fa66.min.js",
		'yaml': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_yaml.7f71c0f462159ba81033.min.js",
		'z80': "https:\/\/a.slack-edge.com\/bv1-1\/codemirror_lang_z80.73d5eb24ebcdece24ced.min.js"
	}		},

		notification_sounds: [{"value":"b2.mp3","label":"Ding","url":"https:\/\/slack.global.ssl.fastly.net\/7e91\/sounds\/push\/b2.mp3","url_ogg":"https:\/\/slack.global.ssl.fastly.net\/46ebb\/sounds\/push\/b2.ogg"},{"value":"animal_stick.mp3","label":"Boing","url":"https:\/\/slack.global.ssl.fastly.net\/7e91\/sounds\/push\/animal_stick.mp3","url_ogg":"https:\/\/slack.global.ssl.fastly.net\/46ebb\/sounds\/push\/animal_stick.ogg"},{"value":"been_tree.mp3","label":"Drop","url":"https:\/\/slack.global.ssl.fastly.net\/7e91\/sounds\/push\/been_tree.mp3","url_ogg":"https:\/\/slack.global.ssl.fastly.net\/46ebb\/sounds\/push\/been_tree.ogg"},{"value":"complete_quest_requirement.mp3","label":"Ta-da","url":"https:\/\/slack.global.ssl.fastly.net\/7e91\/sounds\/push\/complete_quest_requirement.mp3","url_ogg":"https:\/\/slack.global.ssl.fastly.net\/46ebb\/sounds\/push\/complete_quest_requirement.ogg"},{"value":"confirm_delivery.mp3","label":"Plink","url":"https:\/\/slack.global.ssl.fastly.net\/7e91\/sounds\/push\/confirm_delivery.mp3","url_ogg":"https:\/\/slack.global.ssl.fastly.net\/46ebb\/sounds\/push\/confirm_delivery.ogg"},{"value":"flitterbug.mp3","label":"Wow","url":"https:\/\/slack.global.ssl.fastly.net\/7e91\/sounds\/push\/flitterbug.mp3","url_ogg":"https:\/\/slack.global.ssl.fastly.net\/46ebb\/sounds\/push\/flitterbug.ogg"},{"value":"here_you_go_lighter.mp3","label":"Here you go","url":"https:\/\/slack.global.ssl.fastly.net\/7e91\/sounds\/push\/here_you_go_lighter.mp3","url_ogg":"https:\/\/slack.global.ssl.fastly.net\/46ebb\/sounds\/push\/here_you_go_lighter.ogg"},{"value":"hi_flowers_hit.mp3","label":"Hi","url":"https:\/\/slack.global.ssl.fastly.net\/7e91\/sounds\/push\/hi_flowers_hit.mp3","url_ogg":"https:\/\/slack.global.ssl.fastly.net\/46ebb\/sounds\/push\/hi_flowers_hit.ogg"},{"value":"knock_brush.mp3","label":"Knock Brush","url":"https:\/\/slack.global.ssl.fastly.net\/7e91\/sounds\/push\/knock_brush.mp3","url_ogg":"https:\/\/slack.global.ssl.fastly.net\/46ebb\/sounds\/push\/knock_brush.ogg"},{"value":"save_and_checkout.mp3","label":"Whoa!","url":"https:\/\/slack.global.ssl.fastly.net\/7e91\/sounds\/push\/save_and_checkout.mp3","url_ogg":"https:\/\/slack.global.ssl.fastly.net\/46ebb\/sounds\/push\/save_and_checkout.ogg"},{"value":"item_pickup.mp3","label":"Yoink","url":"https:\/\/slack.global.ssl.fastly.net\/7e91\/sounds\/push\/item_pickup.mp3","url_ogg":"https:\/\/slack.global.ssl.fastly.net\/46ebb\/sounds\/push\/item_pickup.ogg"},{"value":"hummus.mp3","label":"Hummus","url":"https:\/\/slack.global.ssl.fastly.net\/7fa9\/sounds\/push\/hummus.mp3","url_ogg":"https:\/\/slack.global.ssl.fastly.net\/46ebb\/sounds\/push\/hummus.ogg"},{"value":"none","label":"None"}],
		alert_sounds: [{"value":"frog.mp3","label":"Frog","url":"https:\/\/slack.global.ssl.fastly.net\/a34a\/sounds\/frog.mp3"}],
		call_sounds: [{"value":"call\/alert_v2.mp3","label":"Alert","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/alert_v2.mp3"},{"value":"call\/incoming_ring_v2.mp3","label":"Incoming ring","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/incoming_ring_v2.mp3"},{"value":"call\/outgoing_ring_v2.mp3","label":"Outgoing ring","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/outgoing_ring_v2.mp3"},{"value":"call\/pop_v2.mp3","label":"Incoming reaction","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/pop_v2.mp3"},{"value":"call\/they_left_call_v2.mp3","label":"They left call","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/they_left_call_v2.mp3"},{"value":"call\/you_left_call_v2.mp3","label":"You left call","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/you_left_call_v2.mp3"},{"value":"call\/they_joined_call_v2.mp3","label":"They joined call","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/they_joined_call_v2.mp3"},{"value":"call\/you_joined_call_v2.mp3","label":"You joined call","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/you_joined_call_v2.mp3"},{"value":"call\/confirmation_v2.mp3","label":"Confirmation","url":"https:\/\/slack.global.ssl.fastly.net\/08f7\/sounds\/call\/confirmation_v2.mp3"}],
		call_sounds_version: "v2",
				default_tz: "America\/Los_Angeles",
		
		feature_tinyspeck: false,
		feature_create_team_google_auth: false,
		feature_enterprise_custom_tos: true,
		feature_webapp_always_collect_initial_time_period_stats: false,
		feature_search_skip_context: false,
		feature_buildy_css: false,
		feature_flannel_use_canary_sometimes: false,
		feature_deprecate_window_cert: true,
		feature_deprecate_window_cert_block: true,
		feature_deprecate_files: false,
		feature_deprecate_get_member_by_name: false,
		feature_usergroup_highlight_words: true,
		feature_prev_reached_end: true,
		feature_modern_upsert_file: true,
		feature_file_threads: false,
		feature_file_threads_cache_update: false,
		feature_more_pins_info: false,
		feature_threads_perf: false,
		feature_message_replies_inline: false,
		feature_subteam_members_diff: true,
		feature_a11y_keyboard_shortcuts: false,
		feature_email_ingestion: false,
		feature_api_site_tools: false,
		feature_msg_consistency: false,
		feature_sidebar_context_menu: false,
		feature_attachments_inline: false,
		feature_fix_files: true,
		feature_channel_eventlog_client: true,
		feature_paging_api: false,
		feature_custom_status_expiry: false,
		feature_m11n_custom_status_input: false,
		feature_sonic_dnd: false,
		feature_enterprise_app_teams: true,
		feature_enterprise_frecency: true,
		feature_ent_app_management_dashboard: true,
		feature_set_away_dialog_behavior: true,
		feature_ent_app_management_restriction: false,
		feature_entitlements: true,
		feature_grid_archive_link_fixes: true,
		feature_dunning: true,
		feature_invoice_dunning: true,
		feature_safeguard_org_retention: true,
		feature_dashboard_sortable_lists: false,
		feature_refactor_admin_stats: false,
		feature_invite_only_workspaces: true,
		feature_leave_workspace_improvements: true,
		feature_enteprise_user_teams_update: false,
		feature_enterprise_org_wide_channels_section: true,
		feature_show_billing_active_for_grid: true,
		feature_find_your_workspace: false,
		feature_compliance_export_helper_copy: false,
		feature_form_text_character_count_copy: false,
		feature_sk_lato_cleanup: false,
		feature_saml_authn_key_expiry_date: true,
		feature_wta_client_support: true,
		feature_xoxa_channel_authorization: true,
		feature_wta_optional_ephemeral_message: false,
		feature_file_links_betterer: false,
		feature_enterprise_dm_deeplink: false,
		feature_session_duration_saved_message: false,
		feature_guest_api_changes: false,
		feature_sso_jit_disabling: true,
		feature_flannel_start_user_specific_props: false,
		feature_channel_alert_words: false,
		feature_connecting_shared_channels_enterprise: false,
		feature_shared_channels_enterprise: false,
		feature_snapshots_the_revenge: false,
		feature_mpim_channels: false,
		feature_esc_connected_workspaces_search: false,
		feature_deprecate_gateways: true,
		feature_conversations_list: true,
		feature_gdpr_user_join_tos: false,
		feature_modernize_admin: false,
		feature_winssb_beta_channel: false,
		feature_slack_astronaut_i18n_jpn: true,
		feature_i18n_customer_stories: false,
		feature_cust_acq_i18n_tweaks: false,
		feature_gdpr_website_update: true,
		feature_gdpr_website_fixes: false,
		feature_gdpr_forget_user: false,
		feature_sales_lp: true,
		feature_presence_sub: true,
		feature_whitelist_zendesk_chat_widget: false,
		feature_live_support_free_plan: false,
		feature_slackbot_goes_to_college: false,
		feature_newxp_enqueue_message: true,
		feature_teambot: false,
		feature_star_shortcut: false,
		feature_show_jumper_scores: true,
		feature_force_ls_compression: false,
		feature_name_tagging_client: true,
		feature_name_tagging_client_autocomplete: false,
		feature_name_tagging_client_topic_purpose: false,
		feature_use_imgproxy_resizing: true,
		feature_share_mention_comment_cleanup: false,
		feature_external_files: false,
		feature_electron_memory_logging: false,
		feature_no_title_markup: true,
		feature_channel_exports: false,
		feature_corp_eng_news: false,
		feature_take_profile_photo: false,
		feature_arugula: false,
		feature_texty_rewrite_on_paste: false,
		feature_deprecate_screenhero: true,
		feature_calls_esc_ui: true,
		feature_toggle_id_translation: true,
		feature_modern_api_q: false,
		feature_default_shared_channels: true,
		feature_default_shared_channels_whats_new: true,
		feature_email_notifications_improvements: true,
		feature_react_lfs: false,
		feature_log_quickswitcher_queries: true,
		feature_enable_mdm: true,
		feature_message_menus: true,
		feature_new_message_click_logging: true,
		feature_announce_only_channels: false,
		feature_app_permissions_backend_enterprise: true,
		feature_token_ip_whitelist: true,
		feature_hide_join_leave: false,
		feature_rollback_to_mapping: false,
		feature_emoji5: true,
		feature_sidebar_theme_undo: false,
		feature_emoji5_dark_launch: true,
		feature_feature_emoji5: false,
		feature_allow_intra_word_formatting: true,
		feature_allow_cjk_autocomplete: true,
		feature_allow_split_word: false,
		feature_i18n_channels_validate_emoji: true,
		feature_slim_scrollbar: false,
		feature_search_query_refinements: true,
		feature_react_search: false,
		feature_prefs_modernization: false,
		feature_sidebar_filters: false,
		feature_sli_channel_archive_suggestions: true,
		feature_unread_counts_without_history: true,
		feature_react_messages: true,
		feature_clipboard_contents: false,
		feature_redux_modals: false,
		feature_react_pin_author: true,
		feature_mrkdwn_truncation: true,
		feature_m11n_channels_join: true,
		feature_m11n_metrics_responsiveness: false,
		feature_react_member_profile_card: false,
		feature_service_import_lfs: false,
		feature_mpdm_default_fe: false,
		feature_channel_notif_dialog_update: false,
		feature_oauth_react_wta: false,
		feature_react_team_picker: false,
		feature_app_index: false,
		feature_app_profile_app_site_link: false,
		feature_custom_app_installs: false,
		feature_gdrive_do_not_install_by_default: true,
		feature_delete_moved_channels: true,
		feature_single_workspace_redirect: true,
		feature_zero_workspace_onboarding: true,
		feature_user_tos: false,
		feature_oom_mv_channels_list: false,
		feature_solr_discoverability: true,
		feature_sso_formatting_error: false,
		feature_single_user_workspace_pagination: true,
		feature_default_workspaces_to_closed: true,
		feature_ms_msg_handlers_profiling: true,
		feature_cross_workspace_quick_switcher_prototype: true,
		feature_org_quick_switcher: false,
		feature_user_prefs_merge_using_custom_callbacks: true,
		feature_ms_latest: true,
		feature_no_preload_video: true,
		feature_guests_use_entitlements: true,
		feature_emoji_picker_frecently_used: false,
		feature_app_space: true,
		feature_app_canvases: false,
		feature_canvases: false,
		feature_stop_loud_channel_mentions: false,
		feature_message_input_byte_limit: false,
		feature_beacon_js_errors: false,
		feature_dialogs_v2_mobile: false,
		feature_user_app_disable_speed_bump: false,
		feature_nudge_team_creators: false,
		feature_onedrive_picker: false,
		feature_lesson_onboarding: true,
		feature_disable_join_notifications: false,
		feature_api_admin_page_not_ent: true,
		feature_faster_channels_browser_render: true,
		feature_non_blocking_user_boot: true,
		feature_non_wasted_flannel_connection: true,
		feature_no_files_info: true,
		feature_less_pins: true,
		feature_runaway_qs: false,
		feature_dark_qs: false,
		feature_delete_team_and_apps: true,
		feature_email_forwarding: true,
		feature_pjpeg: false,
		feature_pdf_thumb: true,
		feature_apps_manage_permissions_scope_changes: true,
		feature_app_dir_only_default_true: false,
		feature_reminder_cross_workspace: false,
		feature_speedy_boot_handlebars: false,
		feature_wta_web_flannel_membership: true,
		feature_better_web_app_model: false,
		feature_channel_invite_modal_cannot_join: false,
		feature_expiring_credits: true,
		feature_email_prefs: true,
		feature_pricing_calculator: false,
		feature_sonic: false,
		feature_flannel_channels_v0: false,
		feature_flannel_always_use_canary: false,
		feature_lazy_channels: false,
		feature_webclient_load_status_site: true,
		feature_react_channel_header: false,
		feature_global_nav: false,
		feature_message_spacing: false,
		feature_shortcuts_flexpane: true,
		feature_app_directory_home_page_redesign: true,
		feature_hidden_wksp_unfurls: false,
		feature_guest_wksp_unfurls: false,
		feature_workspace_scim_management: false,
		feature_email_previewer: false,
		feature_redux_dev_tools: false,
		feature_unified_member: false,
		feature_turn_mpdm_notifs_on: true,
		feature_browser_dragndrop: false,
		feature_granular_shared_channel_perms: false,
		feature_org_detailed_thread_mentions: true,
		feature_force_production_channel: false,
		feature_quill_upgrade: true,
		feature_offline_hint: false,
		feature_aria_msg_summary: false,
		feature_emoji_substr_search: false,
		feature_texty_formatting_commands: false,
		feature_texty_change_queue: false,
		feature_send_button_for_everyone: false,
		feature_shortcuts_prompt: true,
		feature_accessible_dialogs: true,
		feature_app_actions: false,
		feature_app_actions_fe: false,
		feature_app_actions_fe_frecency: false,
		feature_app_actions_response_url: true,
		feature_shared_channel_free_trial_flow: true,
		feature_i18n_compliance_links: false,
		feature_calls_clipboard_broadcasting_optin: true,
		feature_autocomplete_files: true,
		feature_screen_share_needs_aero: false,
		feature_calls_disable_iss_admin: true,
		feature_sidebar_realtime_priority: false,
		feature_in_prod_trials: true,
		feature_billing_ce_request_last4: true,
		feature_sli_explore: false,
		feature_sli_trending_dashboard: false,
		feature_i18n_custom_status: false,
		feature_i18n_select_empty_state_string: false,
		feature_drift_on_plans_page: true,
		feature_cjk_highlight_words: false,
		feature_accessible_fs_dialogs: true,
		feature_channel_browser_dropdown: true,
		feature_slackday_unsent_msg_sync: false,
		feature_trap_kb_within_fs_modals: true,
		feature_date_picker: false,

	client_logs: {"0":{"numbers":[0],"user_facing":false},"2":{"numbers":[2],"user_facing":false},"4":{"numbers":[4],"user_facing":false},"5":{"numbers":[5],"user_facing":false},"23":{"numbers":[23],"user_facing":false},"sounds":{"name":"sounds","numbers":[37]},"37":{"name":"sounds","numbers":[37],"user_facing":true},"47":{"numbers":[47],"user_facing":false},"48":{"numbers":[48],"user_facing":false},"Message History":{"name":"Message History","numbers":[58]},"58":{"name":"Message History","numbers":[58],"user_facing":true},"67":{"numbers":[67],"user_facing":false},"72":{"numbers":[72],"user_facing":false},"73":{"numbers":[73],"user_facing":false},"82":{"numbers":[82],"user_facing":false},"88":{"numbers":[88],"user_facing":false},"91":{"numbers":[91],"user_facing":false},"93":{"numbers":[93],"user_facing":false},"96":{"numbers":[96],"user_facing":false},"99":{"numbers":[99],"user_facing":false},"Channel Marking (MS)":{"name":"Channel Marking (MS)","numbers":[141]},"141":{"name":"Channel Marking (MS)","numbers":[141],"user_facing":true},"Channel Marking (Client)":{"name":"Channel Marking (Client)","numbers":[142]},"142":{"name":"Channel Marking (Client)","numbers":[142],"user_facing":true},"Close Old IMs (Client)":{"name":"Close Old IMs (Client)","numbers":[221]},"221":{"name":"Close Old IMs (Client)","numbers":[221],"user_facing":true},"365":{"numbers":[365],"user_facing":false},"389":{"numbers":[389],"user_facing":false},"438":{"numbers":[438],"user_facing":false},"444":{"numbers":[444],"user_facing":false},"481":{"numbers":[481],"user_facing":false},"488":{"numbers":[488],"user_facing":false},"529":{"numbers":[529],"user_facing":false},"552":{"numbers":[552],"user_facing":false},"dashboard":{"name":"dashboard","numbers":[666]},"666":{"name":"dashboard","numbers":[666],"user_facing":false},"667":{"numbers":[667],"user_facing":false},"773":{"numbers":[773],"user_facing":false},"777":{"numbers":[777],"user_facing":false},"794":{"numbers":[794],"user_facing":false},"Client Responsiveness":{"name":"Client Responsiveness","user_facing":false,"numbers":[808]},"808":{"name":"Client Responsiveness","user_facing":false,"numbers":[808]},"Message Pane Scrolling":{"name":"Message Pane Scrolling","numbers":[888]},"888":{"name":"Message Pane Scrolling","numbers":[888],"user_facing":true},"Unread banner and divider":{"name":"Unread banner and divider","numbers":[999]},"999":{"name":"Unread banner and divider","numbers":[999],"user_facing":true},"1000":{"numbers":[1000],"user_facing":false},"Duplicate badges (desktop app icons)":{"name":"Duplicate badges (desktop app icons)","numbers":[1701]},"1701":{"name":"Duplicate badges (desktop app icons)","numbers":[1701],"user_facing":true},"Members":{"name":"Members","numbers":[1975]},"1975":{"name":"Members","numbers":[1975],"user_facing":true},"lazy loading":{"name":"lazy loading","numbers":[1989]},"1989":{"name":"lazy loading","numbers":[1989],"user_facing":true},"thin_channel_membership":{"name":"thin_channel_membership","numbers":[1990]},"1990":{"name":"thin_channel_membership","numbers":[1990],"user_facing":true},"stats":{"name":"stats","numbers":[1991]},"1991":{"name":"stats","numbers":[1991],"user_facing":true},"ms":{"name":"ms","numbers":[1996]},"1996":{"name":"ms","numbers":[1996],"user_facing":true},"shared_channels_connection":{"name":"shared_channels_connection","numbers":[1999]},"1999":{"name":"shared_channels_connection","numbers":[1999],"user_facing":false},"dnd":{"name":"dnd","numbers":[2002]},"2002":{"name":"dnd","numbers":[2002],"user_facing":true},"2003":{"numbers":[2003],"user_facing":false},"Threads":{"name":"Threads","numbers":[2004]},"2004":{"name":"Threads","numbers":[2004],"user_facing":true},"2005":{"numbers":[2005],"user_facing":false},"Reactions":{"name":"Reactions","numbers":[2006]},"2006":{"name":"Reactions","numbers":[2006],"user_facing":true},"TSSSB.focusTabAndSwitchToChannel":{"name":"TSSSB.focusTabAndSwitchToChannel","numbers":[2007]},"2007":{"name":"TSSSB.focusTabAndSwitchToChannel","numbers":[2007],"user_facing":false},"Presence Detection":{"name":"Presence Detection","numbers":[2017]},"2017":{"name":"Presence Detection","numbers":[2017],"user_facing":true},"mc_sibs":{"name":"mc_sibs","numbers":[9999]},"9999":{"name":"mc_sibs","numbers":[9999],"user_facing":false},"Member searching":{"name":"Member searching","numbers":[90211]},"90211":{"name":"Member searching","numbers":[90211],"user_facing":true},"98765":{"numbers":[98765],"user_facing":false},"8675309":{"numbers":[8675309],"user_facing":false}},


		img: {
			app_icon: 'https://a.slack-edge.com/272a/img/slack_growl_icon.png'
		},
		page_needs_custom_emoji: false,
		page_needs_enterprise: false	};

	
	
	
	
	// i18n locale map (eg: maps Slack `ja-jp` to ZD `ja`)
			boot_data.slack_to_zd_locale = {"en-us":"en-us","fr-fr":"fr-fr","de-de":"de","es-es":"es","ja-jp":"ja"};
	
	// client boot data
		
		
	
	
	
	
	
	// inline_emoji
	boot_data.pref_emoji_mode = "";
	boot_data.pref_jumbomoji = 0;
	boot_data.pref_messages_theme = "";

//-->
</script>
		




		
	<!-- output_js "libs" -->
<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/emoji_5.f765b7e9a668291cfd7b.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/rollup-core_required_libs.af62e9923ce51b4388b1.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>

	<!-- output_js "application" -->
<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/modern.vendor.0f49c13c69baa69c3708.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/application.1d5a2d2ff6bbe0cb5dad.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>

	<!-- output_js "page" -->

		<!-- output_js "core" -->
<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/rollup-core_required_ts.5a3642bdde417e2d3177.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/TS.web.2c57080d6fe5283395da.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/signals.224faae8b29600405855.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>

	<!-- output_js "core_web" -->
<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/rollup-core_web.a85b39d79e64ec97e665.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>

	<!-- output_js "secondary" -->
<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/rollup-secondary_a_required.9b15da5570fdd482bb55.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/rollup-secondary_b_required.47f564d0377c78b3f52e.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>

				
	
	<script type="text/javascript">TS.boot(boot_data);</script>

	<!-- output_js "regular" -->
<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/sticky_nav.f3e5d3f5201730db38d8.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/warn_capslock.e3fce2fe58977d4811e7.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/spin.749a1a852d3b17985a6b.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/ladda.47f0b0a3f70f3894aec8.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>
<script type="text/javascript" src="https://a.slack-edge.com/bv1-1/footer.fc6c556e22abc288b9f4.min.js" crossorigin="anonymous" onload="window._cdn && _cdn.ok(this, arguments)" onerror="window._cdn && _cdn.failed(this, arguments)"></script>


			<script type="text/javascript">
					
				setTimeout(function() {
					$('input[name="email"]').val() ? $('input[name="password"]').focus() : $('input').filter(':visible:first').focus(); 
				}, 100);
			
						
			if (navigator.userAgent.match(/windows phone/i)) {
				$('input[name="password"]').css('font-family', 'sans-serif,arial,verdana,tahoma');
			}
		

		

		var $signin_btn = $('#signin_btn');
		$signin_btn.data('ladda', Ladda.create(document.querySelector('#signin_btn')));

		var no_sso = false;
		var team_id = 'T9HCC7JHH';
		var email_regex = new RegExp("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", 'i');

		// signin form
		$('#signin_form').on('submit', function(e) {

			var email = $.trim($('#email').val());
			var password = $.trim($('#password').val());

			// no email or invalid email
			if (!email || !email_regex.test(email)) {
				$('#email').focus().closest('p').addClass('error');
				e.preventDefault();
				return;
			}

			// no password
			if (!password) {
				$('#password').focus().closest('p').addClass('error');
				e.preventDefault();
				return;
			}

			// Prevent the form from submitting twice, which causes the following SSB signin bug:
			// https://slack-bugs.tinyspeck.com/14961
			$signin_btn.attr('disabled', true);
			$signin_btn.attr('aria-disabled', true);
			$signin_btn.data('ladda').start();
		});

		// magic login signin form
		$('#signin_form_magic').on('submit', function(e) {

			e.preventDefault();
			var email = $.trim($('#email').val());

			// no email or invalid email
			if (!email || !email_regex.test(email)) {
				$('#email').focus().closest('p').addClass('error');
			} else {
				$('[name=email]').val(email);
				$('#magic_login_options .js_insert_email').text(email);
				$('#signin_header, #signin_form, #magic_login_cta, .ssb_password').removeClass('hidden');
				$('#magic_login_options, #signin_form_magic, #email, .browser_password').addClass('hidden');
				$('#magic_login_use_password').focus();
                        }

                });

		// user given magic login, but wants to enter email/password
		$('#magic_login_use_password').on('click', function(e){

			e.preventDefault();
			$('.error').removeClass('error');
			$('#magic_login_options').addClass('hidden');
			$('#signin_form, #signin_header').removeClass('hidden');
			$('#password').focus();

		});

		$('.code_problem').on('click', function (e) {
			e.preventDefault();
			$('.send_code_block').slideToggle();
		});

		$('.view_more_email_domains_button').on('click', function() {
			var $team_email_domains = $('.team_email_domains');
			$team_email_domains.text($team_email_domains.data('team-email-domains-formatted'));
		});

		$(document).ready(function() {
			$forgot_pw = $('#forgot-pw');
			if ($forgot_pw.length) {
				/**
				 * Grab the current email that the user has entered before going to the
				 * 'forgot password' page so that we can prefill the email field.
				 */
				function grabEmail(e) {
					var $el = $(e.target);
					var new_url = $el.attr('href');
					var email = $('#email').val();

					/**
					 * Simple check to make sure that the user actually typed in what looks like an email.
					 * If what the user entered doesn't look like an email, don't prefill.
					 */
					if (email.length > 0 && email.indexOf('@') != -1) {
						new_url += '?email=' + encodeURIComponent(email);
					}

					$el.attr('href', new_url);
				}
				$forgot_pw.on('click', grabEmail);
			}
		});

		
	</script>


<style>.color_9f69e7:not(.nuc) {color:#9F69E7;}.color_4bbe2e:not(.nuc) {color:#4BBE2E;}.color_e7392d:not(.nuc) {color:#E7392D;}.color_3c989f:not(.nuc) {color:#3C989F;}.color_674b1b:not(.nuc) {color:#674B1B;}.color_e96699:not(.nuc) {color:#E96699;}.color_e0a729:not(.nuc) {color:#E0A729;}.color_684b6c:not(.nuc) {color:#684B6C;}.color_5b89d5:not(.nuc) {color:#5B89D5;}.color_2b6836:not(.nuc) {color:#2B6836;}.color_99a949:not(.nuc) {color:#99A949;}.color_df3dc0:not(.nuc) {color:#DF3DC0;}.color_4cc091:not(.nuc) {color:#4CC091;}.color_9b3b45:not(.nuc) {color:#9B3B45;}.color_d58247:not(.nuc) {color:#D58247;}.color_bb86b7:not(.nuc) {color:#BB86B7;}.color_5a4592:not(.nuc) {color:#5A4592;}.color_db3150:not(.nuc) {color:#DB3150;}.color_235e5b:not(.nuc) {color:#235E5B;}.color_9e3997:not(.nuc) {color:#9E3997;}.color_53b759:not(.nuc) {color:#53B759;}.color_c386df:not(.nuc) {color:#C386DF;}.color_385a86:not(.nuc) {color:#385A86;}.color_a63024:not(.nuc) {color:#A63024;}.color_5870dd:not(.nuc) {color:#5870DD;}.color_ea2977:not(.nuc) {color:#EA2977;}.color_50a0cf:not(.nuc) {color:#50A0CF;}.color_d55aef:not(.nuc) {color:#D55AEF;}.color_d1707d:not(.nuc) {color:#D1707D;}.color_43761b:not(.nuc) {color:#43761B;}.color_e06b56:not(.nuc) {color:#E06B56;}.color_8f4a2b:not(.nuc) {color:#8F4A2B;}.color_902d59:not(.nuc) {color:#902D59;}.color_de5f24:not(.nuc) {color:#DE5F24;}.color_a2a5dc:not(.nuc) {color:#A2A5DC;}.color_827327:not(.nuc) {color:#827327;}.color_3c8c69:not(.nuc) {color:#3C8C69;}.color_8d4b84:not(.nuc) {color:#8D4B84;}.color_84b22f:not(.nuc) {color:#84B22F;}.color_4ec0d6:not(.nuc) {color:#4EC0D6;}.color_e23f99:not(.nuc) {color:#E23F99;}.color_e475df:not(.nuc) {color:#E475DF;}.color_619a4f:not(.nuc) {color:#619A4F;}.color_a72f79:not(.nuc) {color:#A72F79;}.color_7d414c:not(.nuc) {color:#7D414C;}.color_aba727:not(.nuc) {color:#ABA727;}.color_965d1b:not(.nuc) {color:#965D1B;}.color_4d5e26:not(.nuc) {color:#4D5E26;}.color_dd8527:not(.nuc) {color:#DD8527;}.color_bd9336:not(.nuc) {color:#BD9336;}.color_e85d72:not(.nuc) {color:#E85D72;}.color_dc7dbb:not(.nuc) {color:#DC7DBB;}.color_bc3663:not(.nuc) {color:#BC3663;}.color_9d8eee:not(.nuc) {color:#9D8EEE;}.color_8469bc:not(.nuc) {color:#8469BC;}.color_73769d:not(.nuc) {color:#73769D;}.color_b14cbc:not(.nuc) {color:#B14CBC;}</style>

<!-- slack-www-hhvm-003831af2a32a662c / 2018-03-24 11:30:50 / v994744788f157f504d4123016987a792d9ade09c / B:H -->


</body>
</html>