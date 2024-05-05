Konser Bilet Sistemi
Bu belge, PyQt6 kullanılarak geliştirilmiş basit bir konser bilet sisteminin dökümantasyonunu içerir. Bu uygulama, kullanıcıların farklı konser etkinliklerine bilet almasını sağlar.

İçindekiler
Giriş
Konser Bilet Sistemi Arayüzü
Konser Sınıfı ve Bilet Sistemi
Ana Program Akışı
Giriş
Bu uygulama, PyQt6 ve Python dilinde geliştirilmiş bir masaüstü uygulamasıdır. Kullanıcılar, çeşitli konser etkinliklerine göz atabilir, istedikleri etkinliği seçebilir ve belirli bir miktar bilet satın alabilirler.

Konser Bilet Sistemi Arayüzü
Arayüz, kullanıcının mevcut konser etkinliklerini listeleyen bir liste ve her etkinlik için ayrıntıları gösteren bir bilgi alanı içerir. Kullanıcılar, bir etkinliği seçtikten sonra kaç bilet almak istediklerini belirleyebilir ve "Bilet Al" düğmesine tıklayarak bilet satın alabilirler.

Konser Sınıfı ve Bilet Sistemi
Konser sınıfı, her konser etkinliğinin adı, mekanı, tarihi, saati, kapasitesi ve mevcut boş bilet sayısını depolar. Bilet sistemi, kullanıcının bilet satın almasını ve biletlerin mevcut durumunu yönetir.

Ana Program Akışı
Program, TicketBookingSystemGUI sınıfından başlar. Kullanıcı, arayüz üzerinden konser etkinliklerini görüntüleyebilir ve bilet satın alabilir. Bilet satın alma işlemi başarıyla tamamlandığında, kullanıcıya bilgi verilir ve boş bilet sayısı güncellenir.
