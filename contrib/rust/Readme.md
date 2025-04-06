Первый эксперимент с получение contrib'а через cargo-vendor
```
$ cargo install cargo-vendor
$ cargo new --lib --name tmp ~/dev/tmp/tmp
$ cargo add --manifest-path ~/dev/tmp/tmp/Cargo.toml anyhow
$ cargo vendor --manifest-path ~/dev/tmp/Cargo.toml contrib/rust
```

ya.make пока рукописный.
