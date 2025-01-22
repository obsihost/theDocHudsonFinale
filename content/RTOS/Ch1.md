
## Definition of Real-Time Systems

- The correctness of real-time systems depends on:
    - **Logical results** of the computation.
    - **Timing** of result production.
- Tasks aim to control or react to events in the real world in real time.
    - Processing must be timely: **neither too late nor too early.**

### Examples of Real-Time Systems

- **Air Traffic Control**
- **Robotics**
- **Vehicle and Train Control**
- **Medical Support Systems**
- **Multimedia Systems**

---

## Characteristics of Real-Time Systems

- **Temporal Constraints:**
    - Deadlines vary based on system types, e.g.:
        - Few milliseconds: Radar systems.
        - 1 second: Machine-man interfaces in aircraft.
        - Hours: Chemical reactions.
        - 24 hours: Weather forecasts.
        - Months/years: Spacecraft operations.

### Comparison: General-Purpose vs. Real-Time Systems

|**General-Purpose Systems**|**Real-Time Embedded Systems**|
|---|---|
|Fairness to all tasks (no starvation).|Meeting deadlines is the primary goal.|
|Optimizing throughput and average performance.|Fairness and throughput are secondary.|
|Worry about overall system efficiency.|Focus on worst-case performance.|

---

## Components of Real-Time Systems

- **Timeliness:** Outputs must meet deadlines.
- **Predictability:** Future consequences of current actions should be known.
- **Testability:** The system should be easily testable for meeting deadlines.
- **Cost Optimality:** Efficient use of resources like energy, memory, etc.
- **Maintainability:** Modular design facilitates modification.
- **Robustness:** Must handle peak loads and exceptions gracefully.
- **Fault Tolerance:** Failures in hardware or software should not cause crashes.

### Importance of Predictability

- **Key Challenge:**
    - System behavior should be predictable.
    - Timing constraints (e.g., deadlines, response times) must be met.
- **Difficulties:**
    - Unpredictable worst-case execution times (e.g., halting problem).
    - Cache behavior, pipelines, and DMA interactions.
    - Interrupt handling introducing delays.
    - **Priority Inversion:** Low-priority tasks blocking high-priority tasks.

---

## Types of Real-Time Tasks

### Hard Real-Time Tasks

- **Definition:** Tasks must complete before the deadline; late completion has zero value.
- **Examples:**
    - Air Traffic Control
    - Vehicle Subsystem Control
    - Nuclear Power Plant Control

### Soft Real-Time Tasks

- **Definition:** Missing deadlines incurs penalties; tardiness reduces system effectiveness.
- **Examples:**
    - Multimedia transmission and reception
    - Networking and telecom systems
    - Computer games

---

## Consequences of Deadline Miss

|**Type**|**Impact**|**Goal**|
|---|---|---|
|**Hard Deadline**|System fails if missed.|Guarantee no deadline miss.|
|**Soft Deadline**|User notices, but the system does not fail.|Meet most deadlines most of the time.|

## Types of Real-Time Tasks

### Periodic Real-Time Tasks

- **Definition:** Tasks repeated at regular intervals.
    - Arrival time: Start of each period.
    - Deadline: End of each period.
    - Execution time: Fixed for each period.
- **Examples:**
    - DRAM charging.
    - System monitoring.

### Aperiodic Real-Time Tasks

- **Definition:** Tasks with irregular arrival times, also called event-driven tasks.
- **Characteristics:**
    - No regular or predictable arrival pattern.
    - Timing constraints depend on the triggering event.
    - Can be preempted by higher-priority tasks.
    - Require flexible resource allocation.
- **Examples:**
    - User input events.
    - Interrupts.

---

## Timing Parameters and Terminology

### Key Parameters:

- **Task Properties:**
    - Period (∆P): Time interval between consecutive releases of a periodic task.
    - Worst-case Execution Time (∆C): Maximum time needed for a task's execution.
    - Relative Deadline (∆D): Maximum time allowed to complete a task after its release.
- **Job Properties:**
    - **Release Time (∆R):** When a job is ready for execution.
    - **Response Time (∆Ri):** Time taken from release to completion.
    - **Absolute Deadline (∆AD):** ∆R + ∆D.
    - **Laxity:** Amount of time a task can wait while still meeting its deadline.
    - **Tardiness:** Time by which a task misses its deadline.

### Simple Task Model Assumptions:

- Tasks are periodic with known periods.
- Tasks are independent of each other.
- Overheads like context switching are negligible.
- Deadlines equal the task period.
- Fixed worst-case execution time for all tasks.

---

## Scheduling and System Models

### Job Lifecycle:

1. **Arrival Time:** When the task becomes ready.
2. **Start Time:** When the task begins execution.
3. **Completion Time:** When the task finishes execution.
4. **Response Time:** Completion time minus arrival time.
5. **Deadline Met:** Completion occurs before absolute deadline.

### Assumptions:

- Single processor system.
- All tasks are periodic.
- Zero context-switching overhead.
- No priority inversion.


## يعني إيه أنظمة rtos؟

- الأنظمة الrtos بتعتمد على:
    - **النتايج الصح بتاعة الحسابات.**
    - **الوقت اللي النتايج دي بتطلع فيه.**
- المهام بتكون عايزة تتحكم في الأحداث أو ترد على الأحداث اللي بتحصل في العالم الحقيقي في نفس الوقت.
    - المعالجة لازم تكون في وقتها: **لا متأخر ولا متقدم.**

### أمثلة على الأنظمة دي

- **مراقبة حركة الطيارات.**
- **الروبوتات.**
- **السيارات والقطارات.**
- **أنظمة الدعم الطبي.**
- **أنظمة المالتيميديا.**

---

## صفات أنظمة الrtos

- **القيود الزمنية:**
    - مواعيد التسليم (الدادلاينز) بتختلف حسب النوع، زي:
        - شوية ميلي ثانية: أنظمة الرادار.
        - ثانية واحدة: التفاعل بين الآلة والبني آدم (زي اللي في الطيارات).
        - ساعات: التفاعلات الكيميائية.
        - 24 ساعة: توقعات الطقس.
        - شهور أو سنين: مركبات الفضاء.

### الفرق بين الأنظمة العادية والزمن الحقيقي

|**الأنظمة العادية**|**الأنظمة الزمن الحقيقي**|
|---|---|
|العدل بين المهام (مفيش مهام تتظلم).|المهم إن المهام تخلص في معادها.|
|تحسين الإنتاجية والأداء العام.|الأداء العام مش مهم لو المهام بتخلص في وقتها.|
|بيركزوا على كفاءة النظام كله.|بيركزوا على أسوأ الحالات.|

---

## مكونات الأنظمة الزمن الحقيقي

- **الالتزام بالمواعيد:** النتايج لازم تطلع في وقتها.
- **التوقع:** لازم نعرف اللي هيحصل بعدين.
- **الاختبار:** لازم نقدر نختبر النظام بسهولة.
- **تكاليف قليلة:** استخدام الموارد زي الطاقة والذاكرة بحكمة.
- **سهولة الصيانة:** تصميم النظام بشكل يسهّل التعديل عليه.
- **الصلابة:** لازم يتحمل الضغوط والمواقف الصعبة.
- **التسامح مع الأخطاء:** لو حصلت مشاكل في الهاردوير أو السوفتوير، النظام مايبوظش.

### أهمية التوقع

- **التحدي الكبير:**
    - سلوك النظام لازم يكون متوقع.
    - القيود الزمنية (زي الدادلاين والاستجابة) لازم تتعمل.
- **الصعوبات:**
    - أوقات التنفيذ السيئة مش دايمًا متوقعة.
    - الكاش والبايبلاينز وDMA بيلعبوا دور.
    - التعامل مع الانقطاعات (Interrupts) ممكن يعمل تأخيرات.
    - **عكس الأولويات:** مهام الأولوية الأقل بتعطل المهام الأعلى.

---

## أنواع المهام الزمن الحقيقي

### المهام اللي لازم تخلص في معادها (Hard Real-Time Tasks)

- **تعريف:** المهام دي لازم تخلص قبل الدادلاين بتاعها؛ لو متأخرة ملهاش قيمة.
- **أمثلة:**
    - مراقبة الطيارات.
    - التحكم في أنظمة العربيات.
    - التحكم في محطات الطاقة النووية.

### المهام اللي بتستحمل شوية تأخير (Soft Real-Time Tasks)

- **تعريف:** لو المهام دي اتأخرت، بيكون فيه عقوبة؛ كل ما التأخير زاد، كل ما العقوبة كانت أكبر.
- **أمثلة:**
    - إرسال واستقبال المالتيميديا.
    - أنظمة الشبكات والاتصالات.
    - ألعاب الكمبيوتر.

---

## لو الدادلاين فات

|**النوع**|**التأثير**|**الهدف**|
|---|---|---|
|**دادلاين صارم**|النظام ينهار لو فات.|ضمان عدم فوات الدادلاين.|
|**دادلاين مرن**|المستخدم ياخد باله، بس النظام مايبوظش.|تحقيق أكبر عدد من الدادلاينز.|

**Low Power Signaling** في الـ **D-PHY** هو نوع من الإشارات اللي بتستخدم في وضع الـ **LP Mode (Low Power Mode)** عشان يتم تقليل استهلاك الطاقة مقارنة بوضع الـ **HS Mode (High-Speed Mode)**.

### طريقة الـ **Low Power Signaling**:

1. **استخدام حالة الإشارة الثابتة (Static Signaling)**:
    
    - في الـ **LP Mode**، الإشارات بتنتقل من خلال التبديل بين حالتين ثابتتين (عادةً **Low** و **High**)، بدلًا من نقل بيانات بسرعة عالية زي اللي بيحصل في الـ **HS Mode**.
    - هذه التبديلات بتكون في صورة **Single-ended Signals**، يعني كل إشارة تُرسل باستخدام قناة واحدة (مش زي في الـ **HS Mode** اللي بتستخدم إشارات Differential).
2. **الفكرة الأساسية**:
    
    - الهدف هو تقليل استهلاك الطاقة عن طريق الحد من التعقيد والسرعة في نقل البيانات.
    - الإشارات في هذا الوضع بسيطة وأقل تأثير على استهلاك الطاقة مقارنة بالـ **High-Speed Lane**.
3. **الـ **LP-0** و **LP-1****:
    
    - في الـ **LP Mode**، فيه حالتين أساسيتين للإشارة:
        - **LP-0**: وهي تمثل الحالة **Low**.
        - **LP-1**: وهي تمثل الحالة **High**.
    - البيانات بيتم تمثيلها باستخدام هاتين الحالتين الثابتتين، ويشبهون ما يحدث في الـ **Idle** عندما لا تكون هناك بيانات مرسلة بشكل نشط.
4. **آلية النقل**:
    
    - البيانات بتنتقل بين الـ **Master** والـ **Slave** (أو جهاز الـ **TX** و **RX**) باستخدام إشارات من خلال قناة منخفضة الطاقة.
    - مش بيتم استخدام **Clock** عالي السرعة في هذه المرحلة، بل بيتم الاكتفاء بالإشارات البسيطة والنقل في حالة **Idle**.
5. **الفائدة من الـ **Low Power Signaling**:
    
    - **توفير الطاقة**: الإشارات بسيطة وقليلة التأثير على استهلاك الطاقة.
    - **تجنب استخدام Clock عالي السرعة**: في هذا الوضع، لا يوجد حاجة لوجود ساعة عالية السرعة مما يساهم في خفض استهلاك الطاقة.

### الخلاصة:

**Low Power Signaling** يعتمد على نقل البيانات باستخدام إشارات ثابتة **LP-0** و **LP-1** عبر قناة منخفضة الطاقة بدلاً من استخدام **High-Speed Differential Signaling** زي اللي بيحصل في الـ **HS Mode**، وبالتالي بيتم تقليل استهلاك الطاقة بشكل كبير.