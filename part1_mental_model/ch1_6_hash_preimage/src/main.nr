use poseidon::poseidon2::Poseidon2;

// Statement: "I know x such that Poseidon2(x) = h".
// x is the witness (private). h is the public input.
fn main(x: Field, h: pub Field) {
    let computed = Poseidon2::hash([x], 1);
    assert(computed == h);
}

#[test]
fn test_correct_preimage() {
    let x = 12345;
    let h = Poseidon2::hash([x], 1);
    main(x, h);
}

// Breaking it on purpose: a wrong x must be rejected.
#[test(should_fail)]
fn test_wrong_preimage() {
    let x = 12345;
    let h = Poseidon2::hash([x], 1);
    main(x + 1, h);
}

// Helper: prints the hash of 12345 so we can use it as the public input.
#[test]
fn print_hash() {
    println(Poseidon2::hash([12345], 1));
}