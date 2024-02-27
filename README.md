WhatsApp Otomatik Mesaj Gönderme # communitymessage
Bu Python kodu, belirli bir zaman diliminde pywhatkit kütüphanesini kullanarak WhatsApp üzerinden otomatik mesaj göndermeyi sağlar. Kodun çalışması için gereken adımları aşağıda bulabilirsiniz:

Telefon Numaralarının Okunması: Kod, phone.txt adlı bir dosyadan telefon numaralarını okur. Her bir satır bir telefon numarasını temsil eder.

Zamanlama Kontrolü: Kod, belirli bir zaman diliminde çalışacak şekilde ayarlanmıştır. Öncelikle, birinci while döngüsü, günün 0.50'sinde yani gece yarısına yakın bir zaman diliminde programı bekletir. Daha sonra, ikinci while döngüsü, günün 2. gününde çalışacak şekilde programı bekletir. Bu, kodun mesajları belirli bir tarihte ve saatte göndermesini sağlar.

Mesaj Gönderme İşlemi: Belirtilen zaman dilimine geldiğinde, her bir telefon numarasına belirli bir mesaj gönderilir. Mesaj içeriği "deneme amacıyla mesaj iceriği" olarak tanımlanmıştır.

Zamanlama Hassasiyeti: Mesajların hemen ardışık saniyelerde gönderilmesi için dakika bilgisine bir artı eklenmiştir. Ancak, bu, pratikte her zaman doğru çalışmayabilir.

Hata Kontrolü ve Optimizasyon: Kodun daha sağlam ve etkili olması için hata kontrolleri eklenmeli ve gerekiyorsa kod optimize edilmelidir.

Bu kod, önceden belirlenmiş bir zaman diliminde otomatik mesaj göndermek için temel bir şablon sağlar. Ancak, kullanmadan önce pywhatkit kütüphanesinin kurulu olduğundan emin olmalısınız ve WhatsApp API'larına erişim izinlerinizin olduğundan emin olmalısınız.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# communitymessage Automated WhatsApp Messaging
This Python script enables automated messaging via WhatsApp using the pywhatkit library within a specified time frame. Below are the steps required for the code to function:

Reading Phone Numbers: The code reads phone numbers from a file named phone.txt. Each line represents a phone number.

Timing Control: The code is set to operate within specific time frames. Initially, the first while loop pauses the program close to midnight, on the 0.50th day of the month. Subsequently, the second while loop pauses the program until the 2nd day of the month. This allows the code to send messages at a specific date and time.

Message Sending Process: When the specified time frame is reached, a particular message is sent to each phone number. The message content is defined as "deneme amacıyla mesaj iceriği".

Timing Precision: An additional minute is added to the minute information to ensure messages are sent in quick succession. However, this may not always work accurately in practice.

Error Handling and Optimization: Error handling should be added for robustness, and the code should be optimized as needed.

This code provides a basic template for sending automated messages within a predetermined time frame. However, before use, ensure that the pywhatkit library is installed and that you have access permissions to the WhatsApp APIs.

