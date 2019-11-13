
const languages = const [
  const Languagee('English', 'en'),
  const Languagee('Tamil', 'ta'),
  const Languagee('Hindi', 'hi'),
  const Languagee('Bengali', 'bn'),
  const Languagee('Gujarati', 'gu'),
  const Languagee('Kannada', 'kn'),
  const Languagee('Malayalam', 'ml'),
];

class Languagee {
  final String name;
  final String code;

  const Languagee(this.name, this.code);
}