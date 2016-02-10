<?php
error_reporting(E_ALL);
ini_set("display_errors", 1);

session_start();

require_once __DIR__.'/../vendor/autoload.php';

$WkmJsonConfig = new wkm\JsonConfig(array("path" => "../conf/"));
$WkmTemplate = new wkm\Template(array(
	"default" => "default_page",
	"extension" => "html",
	"path" => "../templates",
	"twig_options" => array(
			'debug' => true,
			//'cache' => '..cache/templates/compilation_cache',
		)
	)
);

$conf = $WkmJsonConfig->loadDefaultConfiguration();

$app = new Silex\Application();

foreach ($conf["pages"] as $slug => $page) {
	$links = array($slug);
	if(isset($page["default"]) && $page["default"])
		$links[] = "";

	foreach ($links as $link) {
		$app->get("/".$link, function() use ($app, $conf, $slug, $WkmTemplate){
			
			$lang = wkm\get_locale($conf["site"]["default_locale"]);

			return $WkmTemplate->twig->render($WkmTemplate->get_template_link($slug), array(
				"conf" => $conf,
				"page_data" => $conf["locales"][$lang]["pages"][$slug],
				"locale_data" => $conf["locales"][$lang],
				"state" => array(
					"slug" => $slug,
					"locale" => $lang
				)
			));
		});
	}
}

$app->run();