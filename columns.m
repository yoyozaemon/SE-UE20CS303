function [fl1 rq] = columns(aa)


    rq=clip(aa);%Crop the image to size and invert it
    aa=rq;
   
    r=size(aa,2);   %returns no of cloumns
    for s=1:r %execute the for routine from 1 to no. of rows
        if sum(aa(:,s))==0  %checking for empty row  
            for s=s:s+30
                s;
                k=0;
                if sum(aa(:,s))~=0
                    k=1;
                    break
                else   
                end
            end
            if k == 1
                 fl1=~aa;%Only one line.(invert image)
                 rq=[];  %empty the variable re
            else
            nm=aa(1:end,1:s-1);%First line matrix
            rm=aa(1:end,s:end);%Remain line matrix
            fl1=~clip(~nm);
            rq=~clip(~rm);
            %*-*-*Uncomment lines below to see the result*-*-*-*-
                     %imview(fl1);
                     %imview(re);
            break
            end
        else
           
            fl1=~aa;%Only one line.(invert image)
            rq=[];  %empty the variable re
        end
    end
  