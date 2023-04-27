fn main() {}

fn add() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn is_configured() {
        assert_eq!(true, false);
    }
}
