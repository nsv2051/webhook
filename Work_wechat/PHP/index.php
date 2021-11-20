<?php

$url = $_POST['url'];
$title = $_POST['title'];
$description = $_POST['description'];
// 声明页面header
header("Content-type:text/html;charset=utf-8");
 
// 获取access_token
function getToken(){
 
    // 定义id和secret
    $corpid='你的企业微信企业ID';
    $corpsecret='你的应用的secret';
 
    // 读取access_token
    include './access_token.php';
 
    // 判断是否过期
    if (time() > $access_token['expires']){
 
        // 如果已经过期就得重新获取并缓存
        $access_token = array();
        $access_token['access_token'] = getNewToken($corpid,$corpsecret);
        $access_token['expires']=time()+7000;
         
        // 将数组写入php文件
        $arr = '<?php'.PHP_EOL.'$access_token = '.var_export($access_token,true).';'.PHP_EOL.'?>';
        $arrfile = fopen("./access_token.php","w");
        fwrite($arrfile,$arr);
        fclose($arrfile);
 
        // 返回当前的access_token
        return $access_token['access_token'];
 
    }else{
 
        // 如果没有过期就直接读取缓存文件
        return $access_token['access_token'];
    }
}
 
// 获取新的access_token
function getNewToken($corpid,$corpsecret){
    $url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={$corpid}&corpsecret={$corpsecret}";
    $access_token_Arr =  https_request($url);
    return $access_token_Arr['access_token'];
}
 
// curl请求函数
function https_request ($url){
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    $out = curl_exec($ch);
    curl_close($ch);
    return  json_decode($out,true);
}
 
// 发送应用消息函数
function send($data){
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='.getToken());
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    return curl_exec($ch);
}

// 文本卡片消息体
$postdata = array(
    'touser' => '@all',
    'msgtype' => 'textcard',
    'agentid' => '1000002',
    'textcard' => array(
        'title' => $title,
        'description' => $description,
        'url' => $url,
        'btntxt' => '阅读全文',
    ),
    'enable_id_trans' => 0,
    'enable_duplicate_check' => 0,
    'duplicate_check_interval' => 1800
);
 
// 调用发送函数
echo send(json_encode($postdata));
?>