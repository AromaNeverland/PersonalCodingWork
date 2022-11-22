Java.perform(function()
{
    console.log(
        "在https双向认证的情况下，dump客户端证书为p12. 存储位置:/sdcard/Download/client_keystore_{nowtime}.p12 证书密码: fenfei");

Java.use("java.security.KeyStore$PrivateKeyEntry").getPrivateKey.implementation = function()
{
    var
result = this.getPrivateKey();
let
filePath = "/sdcard/Download/client_keystore_" + "_" + getNowTime() + '.p12';
dump2sdcard(this.getPrivateKey(), this.getCertificate(), filePath);
return result;
}

Java.use("java.security.KeyStore$PrivateKeyEntry").getCertificateChain.implementation = function()
{
var
result = this.getCertificateChain();
let
filePath = "/sdcard/Download/client_keystore_" + "_" + getNowTime() + '.p12';
dump2sdcard(this.getPrivateKey(), this.getCertificate(), filePath);
return result;
}
})
