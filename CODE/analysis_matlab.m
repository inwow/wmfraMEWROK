
%% Last Modified: 11 February 2021
%% Written by: Hirdesh Kumar Pharasi
%% Email: hirdeshpharasi@gmail.com
%% Codes can be used to generate the following:
%% (1) index log-returns
%% (2) mean market correlation 
%% (3) GARCH volatility 
%% (4) minimum risk Markowitz portfolio
%% If you are using this code, kindly cite the following article:
%% A. Samal, H.K. Pharasi, S. J. Ramaia, H. Kannan, E. Saucan, J. Jost & A. Chakraborti, Network geometry and market instability, R. Soc. Open Sci. 8: 201734 (2021).
%% To work with moving epochs, we denote Fr: epoch #; Pr: price time series as input; daily_retn= daily logarithmic returns matrix of stock prices
%%
%% function for index returns
%% 
function retn= index_return(Pr,shift,epoch,Fr)
a=shift*(Fr-1)+epoch;
b=a-shift;
retn=log(Pr(a))-log(Pr(b));
end

%% 
%% function for mean correlation
%%