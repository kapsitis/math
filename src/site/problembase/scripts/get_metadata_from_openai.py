from openai import OpenAI
client = OpenAI()
import json

def classify_math_problem(problem_text,prompt_name):
    # Classify the type of math problem using OpenAI
    prompt0 = f"Lūdzu atrodi matemātikas uzdevuma tipu: \n\n ```{problem_text}```\n\n" \
             " Iespējamie jautājumu tipi ir: " \
             "'FindAll' (uzdevumi, kuros jāatrod visi atrisinājumi); " \
             "'FindCount' (uzdevumi, kuros jāsaskaita cik iespēju vai atrisinājumu skaits); " \
             "'FindOptimal' (uzdevumi, kuros jāatrod maksimālais vai minimālais risinājums); " \
             "'FindExample' (uzdevumi, kuros jāatrod 1 piemērs vai pretpiemērs); " \
             "'Prove' (uzdevumi, kuros jāpierāda apgalvojums); " \
             "'ProveDisprove' (uzdevumi, kuros apgalvojums ir jāpierāda vai jāapgāž); " \
             "'Algorithm' (uzdevumi, kuros jāatrod procedūra vai spēles stratēģija)."
    
    prompt1  = "Imagine that you are IMO problem selection committee member - and you are selecting problems for the International Math Olympiad." \
"Your task is to find the most appropriate topic for each problem we specify - whether it is Algebra, Combinatorics, Geometry or Number Theory." \
             "Geometry: Geometry problems in math olympiads often involve creative problem-solving using principles " \
             "of Euclidean geometry. These problems may require the use of geometric properties, theorems, " \
             "and constructions to prove statements or find unknown quantities." \
             "Algebra: Algebra problems typically involve the manipulation and analysis of equations, inequalities, " \
             "and algebraic" \
            "expressions. These problems may require techniques such as factorization, substitution, manipulation " \
             "of " \
              "polynomials, and the application of algebraic identities." \
             "Number Theory: Number theory problems focus on properties and relationships of integers." \
             "These problems often involve divisibility, prime numbers, modular arithmetic, and properties of " \
             "sequences and series." \
             "Combinatorics: Combinatorics problems deal with counting, arranging, and selecting objects. These " \
             "problems may " \
             "involve permutations, combinations, pigeonhole principle, graph theory, and other counting principles." \
             f"Here is a problem you would need to classify: \n\n```{problem_text}```\n\n"
    
    prompt2 = "Iedomājieties, ka esat IMO problēmu atlases komisijas loceklis - un jūs izvēlaties problēmas Starptautiskajai Matemātikas olimpiādei." \
            "Jūsu uzdevums ir atrast vispiemērotāko tēmu katrai problēmai, ko mēs norādām - vai nu tā būtu algebra, kombinatorika, ģeometrija vai skaitļu teorija." \
            "Ģeometrija: Ģeometrijas problēmas matemātikas olimpiādēs bieži vien ietver radošu problēmu risināšanu, izmantojot Eiklīda ģeometrijas principus. " \
            "Šīs problēmas var prasīt ģeometrisko īpašību, teorēmu un konstrukciju izmantošanu, lai pierādītu apgalvojumus vai atrastu nezināmas lielumus." \
            "Algebra: Algebras problēmas parasti ietver vienādojumu, nevienādojumu un algebrisku izteiksmju manipulēšanu un analīzi. " \
            "Šīs problēmas var prasīt tehniskus paņēmienus, piemēram, faktorizāciju, substitūciju, polinomu manipulēšanu un algebrisku identitāšu piemērošanu." \
            "Skaitļu teorija: Skaitļu teorijas problēmas koncentrējas uz veselu skaitļu īpašībām un attiecībām." \
            "Šīs problēmas bieži ietver dalāmību, pirmskaitļus, modulāro aritmetiku un secību un sēriju īpašības." \
            "Kombinatorika: Kombinatorikas problēmas nodarbojas ar objektu skaitīšanu, sakārtošanu un izvēli. " \
            "Šīs problēmas var ietvert permutācijas, kombinācijas, 'vistu būrīša' principu, grafu teoriju un citus skaitīšanas principus." \
            f"Šeit ir problēma, kuru jums būs jāklasificē: \n\n'''{problem_text}'''\n\n"
    
    prompt3 = "Iedomājaties, ka jūs veidojat priekšmetu rādītāju (subject index), " \
             "kas ļauj atrast uzdevumus atbilstoši tajos ierakstītajiem matemātikas terminiem" \
             "katrs termins satur 1-3 vārdus. " \
             "Izvairies no terminiem, kas nebūs vārdnīcās vai vikipēdijas rakstos vai kuri nav matemātiski. " \
            "Dotajam uzdevumam, lūdzu, izrakstiet atrastos terminus no uzdevuma teksta. Seko uzdevuma teksts: \n\n''" \
             f"'{problem_text}'''\n\n"
    
    prompt4 = "For the given math problem please return a list of mathematical concepts. " \
              "Each concept contains 1-3 words and is literally mentioned in the problem text. " \
              "Avoid concepts that are not likely to be in dictionaries or wikipedia articles or are not mathematical. " \
              "Here is the problem: \n\n''" \
              f"'{problem_text}'''\n\n"
    
    prompt5 = "Olympiad problems about number theory are divided into 10 large topics (LTopic) property. We would like to assign a topic to some number theory problems. These are the 10 topics with descriptions:" \
"Label ,DescriptionEn " \
"LTDivisibility - Problems on divisibility relation, distinction of composite and prime numbers. Problems on GCD and LCM; the lattice of all divisors of a fixed number. The expressions for the count and the sum of all divisors for a given number." \
"LTPrimeFactors - Fundamental theorem of arithmetic - prime factors of a number. Checking divisibility through dividing with all the prime powers. Valuation as the highest prime power that divides the given number. " \
"LTNumeralSystems - Decimal notation for integers and digit manipulations. Divisibility rules. Writing a number in binary or other positional notations. Unusual number encodings using Fibonacci, ""negative digits"" and like. Decimal fractions, periodic fraction as a sum of an infinite geometric series. Non-periodic decimals and irrational numbers." \
"LTCongruenceModulo - Modular arithmetic - adding, subtracting, multiplication and raising to a power. The multiplicative inverse of a number by some modulo. Famous theorems about congruences - Little Fermat theorem, Euler theorem, Wilson theorem. " \
"LTTransformsNumTheory - Problems with integer arithmetic using algebraic transformations, factorizations and other identities, variable substitution. Algebraic transformations related to arguments about divisibility and remainders. " \
"LTInequalitiesNumTheory - Applying inequalities and estimates in number theory e.g. to reduce the number of cases to analyze. Expressing boolean conditions for a number with inequalities. Arguing about short intervals (such that between two successive integers there are no other integers). Arguing about long intervals (estimating the number of digits in a number or finding the first digit). " \
"LTEquationsNumTheory - Equations in integer arithmetic, including those solvable with modular arithmetic contradiction. Creating congruence equations. Systems of congruences, Chinese Remainder theorem. Expressing Boolean conditions for a number (last digit, full square, even or odd) with equations or congruences." \
"LTNumTheoryByCases - Problems where the solution analyzes cases by digits, congruence classes or number intervals. Solution methods that allows to eliminate all (but finitely many) solutions. Reasoning with counting cases and Pigeonhole principle in number theory. " \
"LTNumTheoryExamples - Numbers with special properties, using Chinese Remainder theorem to prove existence. Recurrent sequences. Constructing integers and similar objects with regular and structural induction. Algorithms on integers, fast exponentiation algorithm, Bezout identity, extended Euclidean algorithm. Problems with limited repertoire of allowed operations. Functional equations for integer functions." \
"LTIntegerPolynomials - Algera with polynomials with integer coefficients (or taking integer values for integer arguments). Dividing polynomials with remainder; Euclidean algorithm and Bezout identity for polynomials. Eisenstein's criterion for irreducibility. Rational root theorem. Polynomial value difference is divisible by argument difference." \
"Please classify the following problem: \n\n" \
f"'{problem_text}'''\n\n"
              
    
    all_prompts = {'questionType_LV': prompt0, 'domain_EN': prompt1, 'domain_LV' : prompt2, 'concepts_LV' : prompt3, 'concepts_EN' : prompt4, 'LTopics_EN': prompt5}

    response = client.chat.completions.create(
      model="gpt-4-turbo",
      response_format={ "type": "json_object" },
      messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON. JSON should contain one property named 'uzdevuma_tips'"},
        {"role": "user", "content": all_prompts[prompt_name]}
      ]
    )
    print("**********************************")
    data = json.loads(response.choices[0].message.content)
    questiontype_text = data["uzdevuma_tips"]
    print(questiontype_text)
    print("**********************************")
    return questiontype_text


def main():

    # User input
    problem_text = """Uz tāfeles pa reizei uzrakstīti visi naturālie skaitļi no $1$ līdz $n$ ieskaitot. 
Ar vienu gājienu var izvēlēties divus uz tāfeles uzrakstītus skaitļus 
(apzīmēsim tos ar $a$ un $b$), nodzēst tos un to vietā uzrakstīt $\left| a^2-b^2 \right|$. 
Pēc $n-1$ gājiena uz tāfeles paliek viens skaitlis.  
Vai tas var būt $0$, ja **(a)** $n=8$, **(b)** $n=9$?"""

    # Classify the problem
    classify_math_problem(problem_text)


if __name__ == "__main__":
    main()