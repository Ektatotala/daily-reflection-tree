id	parentId	type	text	options	target	signal
START	null	start	Good evening. Let's reflect on your day.			
A1_Q1	START	question	How would you describe your day?	Productive|Tough|Mixed|Frustrating		
A1_D1	A1_Q1	decision		answer=Productive|Mixed:A1_Q2_HIGH;answer=Tough|Frustrating:A1_Q2_LOW		
A1_Q2_HIGH	A1_D1	question	What contributed most to your day?	Planning|Effort|Team support|Adaptability		axis1:internal
A1_Q2_LOW	A1_D1	question	What made your day difficult?	Others' actions|Bad luck|Lack of control|Unexpected issues		axis1:external
A1_R1	A1_Q2_HIGH	reflection	You showed strong ownership today — your actions shaped outcomes.			axis1:internal
A1_R2	A1_Q2_LOW	reflection	It may have felt out of your control, but even then, your responses mattered.			axis1:external
BRIDGE_1_2	A1_R1	bridge	Now let's shift from control to contribution.		A2_Q1	
BRIDGE_1_2B	A1_R2	bridge	Now let's shift from control to contribution.		A2_Q1	

A2_Q1	null	question	Think of one moment today. What best describes it?	I helped someone|I did my work well|I felt under-recognized|I expected more support		
A2_D1	A2_Q1	decision		answer=I helped someone|I did my work well:A2_Q2_HIGH;answer=I felt under-recognized|I expected more support:A2_Q2_LOW		
A2_Q2_HIGH	A2_D1	question	What motivated your action?	Helping others|Team success|Personal satisfaction|Responsibility		axis2:contribution
A2_Q2_LOW	A2_D1	question	What did you expect today?	Recognition|Support|Less workload|Better results		axis2:entitlement
A2_R1	A2_Q2_HIGH	reflection	You focused on contributing — that builds long-term value and trust.			axis2:contribution
A2_R2	A2_Q2_LOW	reflection	It's natural to expect things, but contribution often leads to fulfillment.			axis2:entitlement
BRIDGE_2_3	A2_R1	bridge	Now let's look beyond yourself.		A3_Q1	
BRIDGE_2_3B	A2_R2	bridge	Now let's look beyond yourself.		A3_Q1	

A3_Q1	null	question	When thinking about your day, who comes to mind most?	Myself|My team|A colleague|Customers		
A3_D1	A3_Q1	decision		answer=Myself:A3_Q2_LOW;answer=My team|A colleague|Customers:A3_Q2_HIGH		
A3_Q2_HIGH	A3_D1	question	How did others influence your day?	Collaboration|Support|Shared goals|Helping others		axis3:altro
A3_Q2_LOW	A3_D1	question	What was your main focus today?	My tasks|My stress|My goals|My results		axis3:self
A3_R1	A3_Q2_HIGH	reflection	You showed awareness of others — this builds meaningful work connections.			axis3:altro
A3_R2	A3_Q2_LOW	reflection	Your focus was inward — try expanding your perspective tomorrow.			axis3:self

SUMMARY	null	summary	Today reflected {axis1.dominant} control, {axis2.dominant} contribution, and {axis3.dominant} focus.			
END	SUMMARY	end	Good job reflecting. See you tomorrow.		
