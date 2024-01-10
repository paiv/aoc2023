#!/usr/bin/env ocaml

let sum = List.fold_left (+) 0;;

let lines s = List.filter (fun s -> (String.length s) > 0) (String.split_on_char '\n' s);;

let isdigit = function '0'..'9' -> true | _ -> false;;

let char2int c = int_of_string (String.make 1 c);;

let digits s = String.fold_right (fun c a -> (if isdigit c then (char2int c) :: a else a)) s [];;

let rec firlas xs = match xs with
  | [] -> failwith "nil"
  | [x] -> (x,x)
  | [x;y] -> (x,y)
  | x :: xs -> (x, snd (firlas xs));;

let check s = (let ff = firlas (digits s) in (fst ff) * 10 + (snd ff));;

let part1 data =
  sum (List.map check (lines data));;


let digits s =
  let n = String.length s in
  let sq i c =
    let m = String.length c in
    (i + m) <= n && (String.sub s i m) = c
    in
  let check i c =
    match c with
    | '0' .. '9' -> Some (char2int c)
    | 'o' -> if (sq i "one") then (Some 1) else None
    | 't' -> if (sq i "two") then (Some 2) else
             if (sq i "three") then (Some 3) else None
    | 'f' -> if (sq i "four") then (Some 4) else
             if (sq i "five") then (Some 5) else None
    | 's' -> if (sq i "six") then (Some 6) else
             if (sq i "seven") then (Some 7) else None
    | 'e' -> if (sq i "eight") then (Some 8) else None
    | 'n' -> if (sq i "nine") then (Some 9) else None
    | _ -> None
    in
  let enum a p =
    match (check (fst p) (snd p)) with
    | None -> a
    | Some x -> x :: a
    in
  Seq.fold_left enum [] (String.to_seqi s)

let rxcheck s =
  let ff = firlas (digits s) in
    (snd ff) * 10 + (fst ff);;

let part2 data =
  sum (List.map rxcheck (lines data));;


let test1 = {|
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
|};;
assert ((part1 test1) = 142);;


let test2 = {|
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
|};;
assert ((part2 test2) = 281);;


let () =
  let fn = "day1.in" in
  let data = In_channel.with_open_text fn In_channel.input_all in
(
  let ans = part1 data in
  Printf.printf "%d\n" ans;
  let ans = part2 data in
  Printf.printf "%d\n" ans
);;
