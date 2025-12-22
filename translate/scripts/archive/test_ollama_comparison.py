#!/usr/bin/env python3
"""
Teste comparativo: Llama3.2:3b vs Gemma3:4b
Compara qualidade de tradução e preservação de formatação Markdown
"""

import ollama
import time

# Trecho de teste com todos os elementos problemáticos
TEST_MARKDOWN = """## 🚀 Quick Reference Table

| Workflow | Agent | Track | Purpose |
| -------- | ----- | ----- | ------- |
| **create-ux-design** | UX Designer | BMad Method, Enterprise | Optional UX design |
| **architecture** | Architect | BMad Method, Enterprise | Technical architecture decisions |

### Complete User Journey

**Goal:** Add OAuth social login (Google, GitHub)

**Steps:**

1. **Start:** Load PM agent, say "I want to add OAuth social login"
2. **PM runs tech-spec workflow:**
   - Asks about the feature scope
   - You specify: Google and GitHub OAuth
   - Detects your stack (Next.js 13.4)
   - Generates:
     - tech-spec.md (implementation guide)
     - epics.md (OAuth Integration epic)
3. **Implement:** Load DEV agent
   - DEV implements backend OAuth
   - Done! 👉 🎉

**Total time:** 1-3 hours
"""

SYSTEM_PROMPT = """Você é um tradutor especializado em documentação técnica Markdown.

REGRAS CRÍTICAS:
1. Traduza APENAS o texto em inglês para português brasileiro
2. PRESERVE COMPLETAMENTE a formatação Markdown original:
   - Mantenha todas as tabelas (pipes |)
   - Mantenha toda indentação (espaços antes de -)
   - Mantenha todos os emojis
   - Mantenha todos os links
   - Mantenha todos os code blocks
   - Mantenha todos os hashtags (#, ##, ###)
3. NÃO adicione comentários ou explicações
4. NÃO altere a estrutura do documento
5. Retorne APENAS o Markdown traduzido

Traduza o seguinte documento:"""

def test_model(model_name):
    """Testa um modelo com o trecho de teste"""
    print(f"\n{'='*70}")
    print(f"Testando modelo: {model_name}")
    print(f"{'='*70}\n")
    
    start_time = time.time()
    
    try:
        response = ollama.chat(
            model=model_name,
            messages=[
                {
                    'role': 'system',
                    'content': SYSTEM_PROMPT
                },
                {
                    'role': 'user',
                    'content': TEST_MARKDOWN
                }
            ],
            options={
                'temperature': 0.1,  # Baixa temperatura para tradução mais literal
                'top_p': 0.9,
            }
        )
        
        elapsed = time.time() - start_time
        result = response['message']['content']
        
        print(f"⏱️  Tempo: {elapsed:.1f}s")
        print(f"\n📄 Resultado:\n")
        print(result)
        
        # Análise de preservação
        print(f"\n{'='*70}")
        print("Análise de Preservação:")
        print(f"{'='*70}")
        
        checks = {
            "Tabelas (pipes |)": "|" in result,
            "Emojis (🚀, 👉, 🎉)": "🚀" in result and "👉" in result and "🎉" in result,
            "Hashtags (##, ###)": "##" in result,
            "Indentação (   -)": "   -" in result,
            "Links/formatação": "**" in result,
        }
        
        for check, passed in checks.items():
            status = "✅" if passed else "❌"
            print(f"{status} {check}")
        
        success_rate = sum(checks.values()) / len(checks) * 100
        print(f"\n📊 Taxa de preservação: {success_rate:.0f}%")
        
        return {
            'model': model_name,
            'time': elapsed,
            'result': result,
            'preservation_rate': success_rate,
            'checks': checks
        }
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return None

def main():
    print("="*70)
    print("TESTE COMPARATIVO: Ollama Translation")
    print("="*70)
    print(f"\n📝 Testando com trecho que contém:")
    print("  - Tabelas Markdown")
    print("  - Listas com indentação")
    print("  - Emojis")
    print("  - Formatação (negrito, etc)")
    print("  - Hashtags de títulos")
    
    models = ['llama3.2:3b', 'gemma3:4b']  # Note: gemma2 não gemma3
    results = []
    
    for model in models:
        result = test_model(model)
        if result:
            results.append(result)
        time.sleep(2)  # Pequena pausa entre modelos
    
    # Comparação final
    if len(results) == 2:
        print(f"\n\n{'='*70}")
        print("COMPARAÇÃO FINAL")
        print(f"{'='*70}\n")
        
        for r in results:
            print(f"Modelo: {r['model']}")
            print(f"  Tempo: {r['time']:.1f}s")
            print(f"  Preservação: {r['preservation_rate']:.0f}%")
            print()
        
        # Recomendação
        best = max(results, key=lambda x: x['preservation_rate'])
        fastest = min(results, key=lambda x: x['time'])
        
        print("🏆 RECOMENDAÇÃO:")
        print(f"  Melhor preservação: {best['model']} ({best['preservation_rate']:.0f}%)")
        print(f"  Mais rápido: {fastest['model']} ({fastest['time']:.1f}s)")
        
        if best['model'] == fastest['model']:
            print(f"\n✨ {best['model']} é o vencedor em ambos critérios!")
        else:
            print(f"\n⚖️  Trade-off: Qualidade vs Velocidade")

if __name__ == "__main__":
    main()
