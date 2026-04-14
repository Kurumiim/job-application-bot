# PRD - Job Application Bot

## Visão do Produto
Automatizar o processo de candidatura a vagas, reduzindo tempo humano e aumentando taxa de compatibilidade entre perfil e oportunidades.

## Problema
Processo de candidatura é manual, repetitivo e ineficiente, com baixa taxa de conversão.

## Objetivo
Criar um sistema que:
- leia vagas automaticamente
- compare com currículo estruturado
- gere score de compatibilidade (0-100)
- preencha formulários automaticamente
- permita revisão humana antes do envio

## Usuário alvo
- Profissionais em busca ativa de emprego
- Desenvolvedores e analistas de TI

## MVP (Fase 1)
- upload/import de currículo (PDF ou texto)
- parser de currículo estruturado
- leitura de vagas (URL ou texto)
- engine de score de compatibilidade
- preenchimento automatizado via Playwright
- histórico de candidaturas

## Fora do MVP
- multiusuário
- sistema de pagamento
- dashboard analítico avançado
- automação 100% sem revisão humana

## Critérios de sucesso
- reduzir tempo de candidatura em 80%
- gerar score consistente e explicável
- permitir execução segura com revisão humana

## Riscos
- bloqueio de sites por automação
- variação de formulários
- parsing incorreto de currículo

## Futuro (Fase 2)
- SaaS multiusuário
- IA para otimização de currículo
- ranking de vagas por probabilidade de contratação
