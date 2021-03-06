<?hh


<<__EntryPoint>>
function main_entry(): void {
  require_once("dom_test.inc");

  $dom = new DOMDocument;
  $dom->loadXML(getXmlStr());
  if(!$dom) {
    echo "Error while parsing the document\n";
    exit;
  }

  $node = $dom->documentElement;

  $lang = $node->getAttributeNode('language');
  echo "Language: ".$lang->value."\n";

  $lang->value = 'en-US';
  echo "Language: ".$lang->value."\n";

  $parent = $lang->ownerElement;

  $chapter = new DOMAttr("num", "1");
  $parent->setAttributeNode($chapter);

  echo "Is ID?: ".($chapter->isId()?'YES':'NO')."\n";

  $top_element = $node->cloneNode();

  print $dom->saveXML($top_element);
}
