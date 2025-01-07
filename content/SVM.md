
<div dir="rtl"> 

## **الاثبات كامل**

</div> 



![[SVM-proof.pdf]]


<div dir="rtl"> 


## **شرح طريقة حل الدكتور في السلايدز اللي مش مقتنع بيها بجنيه**
### **1. اختيار الـ Support Vectors**

أول حاجة بنختار نقط (Support Vectors) من الداتا اللي موجودة عندنا ودي بتبقى النقط اللي قريبة من الخط اللي بيفصل بين الclasses
النقط اللي اختارناها هنا:

</div> 


- $\large S_1 = (2, 1)$
- $\large S_2 = (2, -1)$
- $\large S_3 = (4, 0)$

---

<div dir="rtl"> 

### **2. نزود الـ Bias**

علشان نحط الـ bias بنضيف رقم 1 لكل نقطة في الاخر:

</div> 


- $\large \tilde{S}_1 = (2, 1, 1)$
- $\large \tilde{S}_2 = (2, -1, 1)$
- $\large \tilde{S}_3 = (4, 0, 1)$

---

<div dir="rtl"> 

### **3. نكتب المعادلات من الشروط**

بنبني المعادلات على أساس إن:

- الclasses السالبة (-ve) تطلع = -1
- الclasses الموجبة (+ve) تطلع = +1

المعادلات:

</div> 

1. $$\large \alpha_1 \tilde{S}_1 \cdot \tilde{S}_1 + \alpha_2 \tilde{S}_2 \cdot \tilde{S}_1 + \alpha_3 \tilde{S}_3 \cdot \tilde{S}_1 = -1$$
2. $$\large \alpha_1 \tilde{S}_1 \cdot \tilde{S}_2 + \alpha_2 \tilde{S}_2 \cdot \tilde{S}_2 + \alpha_3 \tilde{S}_3 \cdot \tilde{S}_2 = -1$$
3. $$\large \alpha_1 \tilde{S}_1 \cdot \tilde{S}_3 + \alpha_2 \tilde{S}_2 \cdot \tilde{S}_3 + \alpha_3 \tilde{S}_3 \cdot \tilde{S}_3 = +1$$

---

<div dir="rtl"> 

### **4. نعوض بالقيم ونبسط المعادلات**

نحسب الdot product لكل نقطتين وندخل القيم في المعادلات ونبسطها:

</div> 

1. $$\large 6\alpha_1 + 4\alpha_2 + 9\alpha_3 = -1$$
2. $$\large 4\alpha_1 + 6\alpha_2 + 9\alpha_3 = -1$$
3. $$\large 9\alpha_1 + 9\alpha_2 + 17\alpha_3 = +1$$

---

<div dir="rtl"> 
### **5. نحل المعادلات ونطلع قيم ألفا (α)**

بعد الحل:

</div> 

 $$\large \alpha_1 = -3.25,   \alpha_2 = -3.25,  \alpha_3 = 3.5$$

---

<div dir="rtl"> 

### **6. نحسب وزن الخط (w)**

نجيب ال$\large w$ باستخدام المعادلة:

</div>


$$\Large \tilde{w} = \sum \alpha_i \tilde{S}_i$$

<div dir="rtl"> 

نعوض:

</div> 


$$\large \tilde{w} = (-3.25)(2, 1, 1) + (-3.25)(2, -1, 1) + (3.5)(4, 0, 1)$$

<div dir="rtl"> 

نحسبها:

</div> 


$$\large \tilde{w} = (1, 0, -3)$$

---

<div dir="rtl"> 
### **7. معادلة الخط الفاصل (Hyperplane)**

نكتب المعادلة النهائية للخط اللي بيفصل بين الكلاسين:

</div> 


$$\large y = w^T x + b$$

<div dir="rtl"> 

القيم:

</div> 


- $\large w = (1, 0)$
- $\large b = -3$

<div dir="rtl"> 

تبقى المعادلة:

</div> 


$$\large y = x_1 - 3$$

---

<div dir="rtl"> 

### **الخلاصة**
1. اخترنا نقط الSupport Vectors
2. ضفنا لهم bias
3. كتبنا المعادلات اللي بتمثل الفصل بين الكلاسين
4. حلينا المعادلات علشان نطلع قيم الـ $α$
5. حسبنا الوزن $w$ اللي بيحدد الخط الفاصل
6. كتبنا المعادلة النهائية للخط اللي بيفصل بينهم


</div> 