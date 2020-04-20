#Question question 15
#Jagannath Das(DTP)(PhD)
#include<stdio.h>
#include<math.h>
int main()
{
	int i,j,k;
	float a=0,b=2,h=0.1;
	int n=(b-a)/h;
	float y[n+1], t[n+1], y_exact[n+1], error[n+1], error_bound[n+1];
	//Mesh points
	i=0;
	while(i<n+1)
	{
		y[i]=0;		
		t[i]=a+i*h;	 
		i++;
	}
	
	y[0]=0.5;
	i=0;	//Initial condition
	while(i<n+1)
	{
		y[i+1]=y[i]+h*(y[i]-t[i]*t[i]+1);		//soution by euler's method
		y_exact[i]=(t[i]+1)*(t[i]+1)-0.5*exp(t[i]);	//exact solution of the given equation
		error[i]=y_exact[i]-y[i];	             //absolute error
		error_bound[i]=(exp(2)-4)/20*(exp(t[i])-1); // Lipschitz criterion for error bound
		i++;
	}
	
	printf("# of           y_exact     error  error \n");
	printf("iteration                          bound\n");  // setting the required table
	j=0;
	while(j<10)
	{
		printf("%d         %f        %f        %f\n" ,j,y_exact[j],error[j], error_bound[j]);
		j++;
	}
	k=10;
	while(k<n+1)
	{
		printf("%d         %f        %f        %f\n" ,k,y_exact[k],error[k], error_bound[k]);
		k++;
	}
	
	return 0;
}

