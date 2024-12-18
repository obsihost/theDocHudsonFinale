
- The default timing of the clocking block is to sample inputs with a skew of  1step and to drive the outputs with a delay of #0

- #### you can remember this by imagining that the clocking block inserts a synchronizer between the design and testbench

- You should always drive interface signals in a clocking block with a synchronous drive using a nonblocking assignment. This is because the design signal does not change immediately after your assignment

- الفكره اني لو ماستخدمتش non-blocking assignment ايه اللي هيحصل؟
- علي سبيل المثال لو انا عندي clocking block خاص ب ال test bench بحيث ان ال request signal خارجه من ال test bench (clocking block ) ورايحه لل DUT(Arbiter)

![[Pasted image 20241009162337.png]]

-  لو ال output بتاع ال clocking block  (arb_if.request) اتغير عند ال edge بالظبط و انا مستخدم blocking assignment  ف ال input signal اللي داخله لل DUT اتغيرت قيمتها عند ال edge بالظبط  و مش هتاخد في اعتبارها ال  output skew
- عشان كده الصح اننا نستخدم ال NBA عشان لو غيرت ال clocking block output عند ال edge بالظبط مايحصلش propagation لل value و ياخد في اعتباره ال output skew ف يخلي ال value القديمه هي اللي ت propagate و ال value الجديده تستنا لل cycle الجايه 

If you want to wait for two clock cycles before driving a signal, you can either use “ repeat (2) @arbif.cb ;” or use the cycle delay ##2 .