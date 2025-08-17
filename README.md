# Merge Sort Algoritması

Bu proje Merge Sort (Birleştirme Sıralaması) algoritmasının Python implementasyonunu içerir.

## Algoritma Hakkında

Merge Sort, böl ve yönet (divide and conquer) paradigmasını kullanan etkili bir sıralama algoritmasıdır.

### Nasıl Çalışır?

1. **Böl**: Diziyi recursively ikiye böl
2. **Yönet**: Alt dizileri sırala
3. **Birleştir**: Sıralı alt dizileri birleştir

## Kullanım

```bash
python merge_sort.py
```

## Örnek Çıktı

```
=== MERGE SORT AŞAMALARI ===
Orijinal dizi: [16, 21, 11, 8, 12, 22]

--- Adım Adım İşlem ---
Böl: [16, 21, 11, 8, 12, 22]
Sol: [16, 21, 11], Sağ: [8, 12, 22]
  Böl: [16, 21, 11]
  Sol: [16], Sağ: [21, 11]
    Böl: [16]
    Sonuç: [16]
    Böl: [21, 11]
    Sol: [21], Sağ: [11]
      Böl: [21]
      Sonuç: [21]
      Böl: [11]
      Sonuç: [11]
    Birleştir: [11, 21]
  Birleştir: [11, 16, 21]
  Böl: [8, 12, 22]
  Sol: [8], Sağ: [12, 22]
    Böl: [8]
    Sonuç: [8]
    Böl: [12, 22]
    Sol: [12], Sağ: [22]
      Böl: [12]
      Sonuç: [12]
      Böl: [22]
      Sonuç: [22]
    Birleştir: [12, 22]
  Birleştir: [8, 12, 22]
Birleştir: [8, 11, 12, 16, 21, 22]

Son sonuç: [8, 11, 12, 16, 21, 22]
```

## Karmaşıklık Analizi

| Durum | Zaman Karmaşıklığı | Yer Karmaşıklığı |
|-------|-------------------|------------------|
| En İyi | O(n log n) | O(n) |
| Ortalama | O(n log n) | O(n) |
| En Kötü | O(n log n) | O(n) |

## Avantajları

- Stabil sıralama algoritması
- Guaranteed O(n log n) performans
- Büyük veri setleri için uygun

## Dezavantajları

- O(n) ek bellek gereksinimi
- Küçük diziler için overhead
