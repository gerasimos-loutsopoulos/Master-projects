/* -*- Mode:Prolog; coding:iso-8859-1; indent-tabs-mode:nil; prolog-indent-width:8; prolog-paren-indent:4; tab-width:8; -*- 
Constraint store

Author: Tony Lindgren

*/
:- use_module([library(clpfd)]).


zebra:-
        % Define variabels and their domain      
        House_colors = [Red, Green, White, Yellow, Blue],
        domain(House_colors, 1, 5),  
	%TODO - add more varaibels and their domains	
		
	Nationality =[English,Swede,Dane,Norwegian,German],
	domain(Nationality, 1, 5), 
	Drinks = [Tea, Milk, Coffee, Water, Beer], 
	domain(Drinks, 1, 5), 
	Smokes = [PallMall,Dunhill, Blend, Prince, BlueMaster],
	domain(Smokes, 1,5),
	Pet = [Dog, Birds, Cats, Horse, Zebra],
	domain(Pet, 1, 5),
		
        % Define constraints and relations
        all_different(House_colors),
        all_different(Nationality),
        all_different(Drinks),
        all_different(Smokes),
        all_different(Pet),
       
    
        Red #= English, 
        Swede #= Dog,
        Dane #= Tea,
        (Green #= White - 1), 
        Coffee #= Green,
        PallMall #= Birds,
        Yellow #= Dunhill,
        Milk #= 3, % In the middle house they drink milk., correct??
        Norwegian #= 1, % The Norwegian lives in the first house, correct??
        (Blend #= Cats - 1 ; Blend #= Cats + 1), 
        (Horse #= Dunhill - 1 ; Horse #= Dunhill + 1),
        BlueMaster #= Beer, 
        German #= Prince, 
        (Norwegian #= Blue - 1 ; Norwegian #= Blue + 1), % ?
        (Water #= Blend - 1; Water #= Blend + 1), % ?
 
       	%TODO - add more constraints and relations	
        % append variables to one list
        
        append(House_colors, Nationality, Temp1),
        append(Temp1, Pet, Temp2),
        append(Temp2, Drinks, Temp3), 
        
	%TODO - append all variabels
        append(Temp3, Smokes, VariableList),
        
        % find solution
        labeling([], VariableList), 
                                                  
        % connect answers with right objects
        sort([Red-red, Green-green, White-white, Yellow-yellow, Blue-blue], House_color_connection),
        sort([English-english, Swede-swede, Dane-dane, Norwegian-norwegian, German-german], Nation_connection),  
        
        sort([Tea-tea, Milk-milk, Coffee-coffee, Water-water, Beer-beer], Drink_connection),
        sort([Dog-dog, Birds-birds, Cats-cats, Horse-horse, Zebra-zebra], Pet_connection),
        sort([PallMall-pallmall, Dunhill-dunhill, Blend-blend, Prince-prince, BlueMaster-bluemaster], Smokes_connection),
		%TODO - add sorting of all variabels
		
		
        % print solution
        Format = '~w~15|~w~30|~w~45|~w~60|~w~n',
        format(Format, ['house 1', 'house 2', 'house 3', 'house 4', 'house 5']),
        format(Format, House_color_connection),
	%TODO - print of all variabels
	format(Format, Drink_connection),
	format(Format, Pet_connection),
	format(Format, Smokes_connection),
        format(Format, Nation_connection).


        






    
        


    


        



                                                              

            
        